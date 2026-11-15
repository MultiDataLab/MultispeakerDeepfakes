# MaSC: Multi-Speaker Conversational Partial Audio Deepfake Dataset

MaSC is a research dataset for studying **partial audio deepfake detection and temporal localization in multi-speaker conversations**. It contains authentic conversational recordings paired with manipulated counterparts in which one short phrase has been replaced by synthetic speech.

## Dataset overview

| Property | Description |
|---|---|
| Total audio clips | 2,168 |
| Authentic clips | 1,084 |
| Partially manipulated clips | 1,084 |
| Pairing | One authentic clip and one corresponding manipulated clip |
| Typical clip duration | Approximately 10 seconds (one shorter clip) |
| Manipulation | Single localized phrase replacement |
| Speech synthesis | XTTS v2, conditioned on reference speech from the intended speaker |
| Annotation | Clip-level authenticity labels and annotated manipulation start/end times |
| Source recordings | Two parent recordings of conversational English-learning material |
| Research tasks | Clip-level detection and temporal localization |

## Dataset construction

The authentic clips were extracted from conversational English-learning videos. Permission to use the source audio for the research project was obtained from the creator. Each manipulated counterpart was constructed by replacing a localized spoken phrase with XTTS v2-generated speech conditioned on the intended speaker. The replacement was duration-matched, level-aligned, and crossfaded; surrounding conversational content was retained.

The corpus contains **1,084 paired examples**, not 2,168 independent conversations. Its two parent recordings may contain shorter compiled conversations, and global speaker independence has not been established.

## Repository structure

```text
MaSC/
├── README.md
├── CITATION.bib
├── Audio_samples/
│   └── README.md
├── Audio/
│   └── README.md
└── metadata/
    └── README.md
```

- **Audio_samples/**: Location for an optional small example set, only if public redistribution is authorized.
- **Audio/**: Dataset access and availability information. Full audio is not bundled with this template.
- **metadata/**: Description of clip labels and timestamp annotations; files will be added when cleared for release.

## Suggested evaluation protocol

The study uses a parent-separated partition: **501 authentic/manipulated pairs (1,002 clips)** from one parent recording for training, and **583 pairs (1,166 clips)** from another for testing. Related clips and their counterparts are kept together. This reduces direct parent-recording overlap but does not establish independence of underlying speakers or original conversations.

The exact partition manifest should accompany any public benchmark release to enable reproducibility.

## Availability and permissions

**Dataset audio is not included in this repository template.** Permission to use source recordings for a research project does not necessarily grant permission to redistribute the audio or manipulated derivatives publicly. Audio samples and download links should only be added after the relevant distribution permissions and institutional requirements have been confirmed.

Metadata, code, and documentation may be released separately from audio, subject to any applicable restrictions.

## Research paper

**MaSC: An Audio Dataset for Multi-Speaker Conversational Partial Audio Deepfake Detection and Localization**  
Accepted for IEEE BigData 2026; publication details pending.

## Citation

Until the proceedings publication is available, cite the MaSC dataset repository (see [`CITATION.bib`](CITATION.bib)). Once the paper is published, this section can be updated with the final bibliographic reference and DOI.

## Responsible use

This dataset is intended for research on synthetic-speech detection, localization, and robustness. It should not be used to impersonate real speakers, misrepresent speech as authentic, or violate the source creator's permissions.
