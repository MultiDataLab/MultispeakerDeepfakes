# MsCADD: Multi-Speaker Conversational Audio Deepfake Dataset

This folder contains the **MsCADD dataset**, introduced in our paper:

> Alabi J. Ahmed, Sanjay Purushotham , Vandana Janeja  
> *Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study*  
> Accepted at ICDM MLC Workshop 2025

---

## 📂 Folder Structure

- **Audio_samples/**  
  A small demo subset of the dataset (organized into `fake/` and `real/`).  
  These are provided for quick inspection and testing.

- **Audio/**  
  Contains a text file with links to download the **full dataset**.  

- **README.md**  
  You are here — overview and usage instructions for MsCADD.

---

## 🎧 Dataset Description

- **Total clips**: 2,830 audio conversations  
  - 1,148 **real** human-recorded dialogues  
  - 1,682 **synthetic** conversations generated via TTS

- **Duration**: Each clip is 10–22 seconds long.  
- **Speakers per clip**: 2  
- **Speaker composition**:  
  - Male–Female  
  - Male–Male  
  - Female–Female  

- **Sources**:  
  - Real conversations from the English Conversation Corpus (ICASSP 2022)  
  - Synthetic conversations generated with:  
    - **VITS (Coqui TTS)** – multiple speaker IDs for timbre/accent diversity  
    - **SoundStorm (Google NotebookLM TTS)** – natural back-and-forth exchanges including laughter and conversational nuances  

---

## 📊 Benchmark Baselines

We provide results for three neural baseline detection models:  
- **LFCC-LCNN** (ASVspoof baseline)  
- **RawNet2** (end-to-end CNN)  
- **Wav2Vec 2.0** (self-supervised transformer)  

Performance metrics include accuracy, F1-score, TPR, and TNR. See our paper for details.

---

## 🔗 Download

- Full dataset (all 2,830 clips) is available via the links in the **`Audio/`** folder.  
- Sample subset is included under **`Audio_samples/`** for quick testing.  

---

## 📜 Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{ahmed2025mscadd,
  title={Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study},
  author={Ahmed, Alabi and Purushotham, Sanjay and Janeja, Vandana},
  booktitle={ICDM Workshop on Machine Learning for Cybersecurity (MLC)},
  year={2025}
}

