# MultispeakerDeepfakes Project

This repository hosts research artifacts, datasets, and resources from the **MultiDataLab** related to **multi-speaker conversational audio deepfakes**.  
Our long-term goal is to build a comprehensive collection of benchmarks, models, and tools to advance research in this underexplored area.

---

## 📌 Current Release

### MsCADD: Multi-Speaker Conversational Audio Deepfake Dataset
- **2,830 audio clips** (1,148 real + 1,682 synthetic) of two-speaker conversations.
- Synthetic clips generated using **VITS** and **SoundStorm (NotebookLM)** to simulate natural multi-speaker exchanges.
- Includes **metadata** for speaker composition, source model, and dataset splits.
- Benchmarked with LFCC-LCNN, RawNet2, and Wav2Vec 2.0 baselines.

📂 Access here: [MsCADD folder](./MsCADD)  
📖 Paper: *Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study* (ICDM MLC Workshop 2025)  

---

## 🚀 Roadmap

This repository will grow to include:
- **Extended datasets** covering partial manipulations, multi-speaker voice conversion, and noisy/overlapped conversations.
- **Baseline models and benchmarks** for comparison with new detection methods.
- **Research code** for reproducibility and community contributions.

---

## 📜 Citation

If you use our dataset or resources, please cite:

```bibtex
@inproceedings{ahmed2025mscadd,
  title={Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study},
  author={Ahmed, Alabi J. and Purushotham, Sanjay and Janeja, Vandana},
  booktitle={ICDM Workshop on Machine Learning for Cybersecurity (MLC)},
  year={2025}
}
