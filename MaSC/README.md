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
| Research tasks | Clip-level detection and temporal localization |

## Dataset construction

The authentic clips were extracted from conversational English-learning videos. Permission to use the source audio for the research project was obtained from the creator. Each manipulated counterpart was constructed by replacing a localized spoken phrase with XTTS v2-generated speech conditioned on the intended speaker. The replacement was duration-matched, level-aligned, and crossfaded; surrounding conversational content was retained.

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

- **Audio_samples/**: Small sample set.
- **Audio/**: Dataset access and availability information.
- **metadata/**: Description of clip labels and timestamp annotations.


## Research paper

**MaSC: An Audio Dataset for Multi-Speaker Conversational Partial Audio Deepfake Detection and Localization**  
IEEE BigData 2026.


## Responsible use

This dataset is intended for research on synthetic-speech detection, localization, and robustness. It should not be used to impersonate real speakers, misrepresent speech as authentic, or violate the source creator's permissions.
