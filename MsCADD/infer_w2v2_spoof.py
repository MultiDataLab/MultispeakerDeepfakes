import argparse, os, math, warnings
from pathlib import Path
import numpy as np
import librosa
import torch
import torch.nn.functional as F
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import pandas as pd
from tqdm import tqdm

warnings.filterwarnings("ignore")

def load_audio(path, target_sr):
    y, sr = librosa.load(path, sr=target_sr, mono=True)
    return y

def chunk_logits(logits_list):
    logits = torch.stack(logits_list, dim=0).mean(dim=0)
    probs = F.softmax(logits, dim=-1).cpu().numpy()
    return logits, probs

def main(args):
    device = "cuda" if torch.cuda.is_available() and not args.cpu else "cpu"
    print(f"Using device: {device}")

    model_id = args.model_id
    print(f"Loading model: {model_id}")
    processor = AutoFeatureExtractor.from_pretrained(model_id)
    model = AutoModelForAudioClassification.from_pretrained(model_id).to(device)
    model.eval()

    id2label = model.config.id2label
    label_names = [id2label[i] for i in range(len(id2label))]
    print(f"Model labels: {label_names}")

    def guess_label_index(name_candidates):
        idx = None
        for n in name_candidates:
            for i, nm in id2label.items():
                if n == nm.lower():
                    idx = i
                    break
            if idx is not None:
                break
        return idx

    fake_idx = guess_label_index(["spoof", "fake", "deepfake", "spoofed"])
    real_idx = guess_label_index(["bonafide", "real", "genuine"])
    if fake_idx is None or real_idx is None:
        print("⚠️ Could not auto-detect real/fake label indices.")
        fake_idx = args.fake_idx
        real_idx = args.real_idx

    target_sr = getattr(processor, "sampling_rate", 16000)
    print(f"Target sampling rate: {target_sr}")

    dataset_root = Path(args.dataset_dir)
    real_dir = dataset_root / "real"
    fake_dir = dataset_root / "deepfake"

    files = []
    for p in sorted(real_dir.rglob("*")):
        if p.suffix.lower() in [".wav", ".flac", ".mp3", ".m4a"]:
            files.append((str(p), 0))
    for p in sorted(fake_dir.rglob("*")):
        if p.suffix.lower() in [".wav", ".flac", ".mp3", ".m4a"]:
            files.append((str(p), 1))

    assert len(files) > 0, f"No audio found in {dataset_root}/real and {dataset_root}/deepfake"

    results = []
    y_true, y_score, y_pred = [], [], []
    max_chunk_sec = args.max_chunk_sec
    max_chunk_len = int(max_chunk_sec * target_sr)

    for path, true_label in tqdm(files, desc="Infer"):
        try:
            y = load_audio(path, target_sr)
            logits_list = []
            if len(y) == 0:
                raise ValueError("empty audio")
            num_chunks = math.ceil(len(y) / max_chunk_len)
            for i in range(num_chunks):
                s = i * max_chunk_len
                e = min((i+1)*max_chunk_len, len(y))
                y_chunk = y[s:e]
                if len(y_chunk) < 1600:
                    continue
                inputs = processor(y_chunk, sampling_rate=target_sr, return_tensors="pt")
                with torch.no_grad():
                    out = model(**{k: v.to(device) for k, v in inputs.items()})
                    logits_list.append(out.logits.squeeze(0))
            if not logits_list:
                raise ValueError("no valid chunks")
            logits, probs = chunk_logits(logits_list)
            pred_idx = int(np.argmax(probs))
            if fake_idx is not None and real_idx is not None:
                prob_fake = float(probs[fake_idx])
                prob_real = float(probs[real_idx])
            else:
                order = np.argsort(-probs)
                prob_fake = float(probs[order[0]]) if label_names[order[0]].lower() in ["spoof","fake","deepfake","spoofed"] else float(probs[order[1]]) if len(order)>1 else 0.0
                prob_real = float(probs[order[0]]) if label_names[order[0]].lower() in ["bonafide","real","genuine"] else float(probs[order[1]]) if len(order)>1 else 0.0

            results.append({
                "path": path,
                "true_label": true_label,
                "pred_label_idx": pred_idx,
                "pred_label_name": id2label[pred_idx],
                "prob_fake": prob_fake,
                "prob_real": prob_real
            })
            y_true.append(true_label)
            y_score.append(prob_fake if fake_idx is not None else float(probs[1]) if len(probs)>1 else float(probs[pred_idx]))
            y_pred.append(1 if (fake_idx is not None and pred_idx == fake_idx) else (pred_idx))
        except Exception as e:
            results.append({
                "path": path,
                "true_label": true_label,
                "error": str(e)
            })

    out_csv = Path(args.out_csv)
    pd.DataFrame(results).to_csv(out_csv, index=False)
    print(f"Saved results to {out_csv}")

    mask = [("error" not in r) for r in results]
    y_true_eval = np.array([r["true_label"] for r, m in zip(results, mask) if m])
    y_pred_eval = np.array([p for p, m in zip(y_pred, mask) if m])
    y_score_eval = np.array([s for s, m in zip(y_score, mask) if m])

    if len(y_true_eval) > 0:
        print("\nConfusion matrix [ [TN FP]; [FN TP] ]:")
        print(confusion_matrix(y_true_eval, y_pred_eval))
        print("\nClassification report:")
        print(classification_report(y_true_eval, y_pred_eval, target_names=["real(0)","fake(1)"]))
        if len(np.unique(y_true_eval)) == 2:
            auc = roc_auc_score(y_true_eval, y_score_eval)
            print(f"ROC-AUC: {auc:.4f}")
    else:
        print("No valid predictions to evaluate.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_id", type=str, required=True,
                        help="HuggingFace model id for a Wav2Vec2 anti-spoofing model")
    parser.add_argument("--dataset_dir", type=str, default="Dataset")
    parser.add_argument("--out_csv", type=str, default="inference_results.csv")
    parser.add_argument("--max_chunk_sec", type=float, default=15.0,
                        help="Chunk length in seconds for long files")
    parser.add_argument("--cpu", action="store_true", help="Force CPU")
    parser.add_argument("--fake_idx", type=int, default=None)
    parser.add_argument("--real_idx", type=int, default=None)
    args = parser.parse_args()
    main(args)
