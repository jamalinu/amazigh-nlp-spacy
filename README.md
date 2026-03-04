# 🌍 Amazigh/Berber NLP Pipeline with spaCy

> First open-source NLP pipeline for Tamazight (Amazigh/Berber language)
> built by a native speaker with formal linguistics training.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/advanced_morphology_tamazight.ipynb)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/jamalinu/amazigh-nlp-demo)
[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-orange)](https://huggingface.co/jamalinu/advanced_morphology_tamazight)
[![Hugging Face Dataset](https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-green)](https://huggingface.co/datasets/jamalinu/tarifit-pbc-corpus)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Tarifit](https://img.shields.io/badge/Language-Tarifit%20Berber-green)](https://en.wikipedia.org/wiki/Tarifit)

---

## 🎯 Why this project matters

Tamazight is spoken by **30+ million people** across North Africa, yet has
virtually zero computational linguistics resources. This project addresses
that gap by combining:

- Native speaker linguistic knowledge (Tamazight, Arabic, Spanish, French, Catalan)
- Formal philology and linguistics training
- Modern NLP tools (spaCy, scikit-learn, Python)

---

## 🔬 What this project includes

| Module | Description | Status |
|--------|-------------|--------|
| Tokenizer | Custom Tamazight tokenizer | ✅ Done |
| NER | Named Entity Recognition (people, places) | ✅ Done |
| Sentiment Analysis | Positive / Negative / Neutral classifier | ✅ Done |
| Tarifit Morphology | Clitic tokenizer + POS + Morpheme segmenter | ✅ Done |
| **PBC Corpus** | **57 phonetically balanced sentences for TTS** | ✅ **Done** |

---

## 🚀 Live Demo

Try all tools here → **[amazigh-nlp-demo on Hugging Face](https://huggingface.co/spaces/jamalinu/amazigh-nlp-demo)**

| Tool | Description |
|------|-------------|
| 🔎 **Named Entity Recognizer** | Detects people (PER) and locations (LOC) |
| 🎭 **Sentiment Analyzer** | Classifies comments as Positive, Negative or Neutral |
| 🏔️ **Tarifit Morphology Analyzer** | Clitics, POS tagging, morpheme segmentation, interlinear gloss |

---

## 🗄️ Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| tarifit-pbc-corpus | 57 phonetically balanced sentences for Tarifit TTS · IPA transcriptions · 100% phoneme coverage | [![Hugging Face](https://img.shields.io/badge/🤗-Dataset-green)](https://huggingface.co/datasets/jamalinu/tarifit-pbc-corpus) |

---

## 📓 Notebooks

### 01 — Foundations: Initial Setup & spaCy Basics
Introduction to the working environment and loading the multilingual base model.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/01_fundamentos_spacy_amazigh.ipynb)

---

### 02 — Advanced Morphological Tokenization
Solving Amazigh-specific linguistic challenges: clitic segmentation and Tifinagh character normalization.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/02_morfologia_avanzada.ipynb)

---

### 03 — Named Entity Recognition (NER) for Tamazight
Identification of toponyms (Rif) and historical figures in Latin and Tifinagh scripts.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/03_ner_amazigh.ipynb)

---

### 04 — Sentiment Analysis — Tamazight Social Comments
First sentiment classifier for Tamazight. Labels: Positive / Negative / Neutral.
Built with TF-IDF + Naive Bayes and a custom Tamazight sentiment lexicon.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/04_sentiment_tamazight.ipynb)

---

### 05 — Advanced Morphology Tamazight (Tarifit) ⭐
Custom tokenizer for Berber clitics, POS tagging, morpheme segmentation and displaCy visualization.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/advanced_morphology_tamazight.ipynb)

| Step | Content |
|------|---------|
| 1 | Environment setup — spaCy blank model |
| 2 | Berber morphology theory — clitic types and structure |
| 3 | `TarifitTokenizer` — separates proclitics and enclitics |
| 4 | `TarifitMorphAnalyzer` — POS tagging with lexicon + patterns |
| 5 | `MorphemeSegmenter` — prefix · root · suffix · consonantal root |
| 6 | displaCy visualization — color-coded POS and dependency trees |

```
Input:   ur ffigh ara ddarwi
Tokens:  [ur]=NEG  [ffigh]=VERB  [ara]=NEG2  [ddarwi]=ADV
Gloss:   NEG   go.out   NEG2   together
English: "We did not go out together"
```

---

### 06 — Phonetically Balanced Corpus for TTS ⭐ NEW
First phonetically balanced corpus for Tarifit. 57 sentences with IPA transcription
designed for Text-To-Speech training. 100% phoneme coverage.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/tarifit_pbc_corpus.ipynb)
[![Dataset](https://img.shields.io/badge/🤗-tarifit--pbc--corpus-green)](https://huggingface.co/datasets/jamalinu/tarifit-pbc-corpus)

| Step | Content |
|------|---------|
| 1 | Tarifit phoneme inventory — 27 phonemes |
| 2 | 57 sentences — 12 sentence types |
| 3 | Phoneme coverage analysis — Counter + regex |
| 4 | Visualization with matplotlib |
| 5 | Export — CSV, Coqui TTS format, recording script |

```
Coverage: 27/27 phonemes — 100%
Sentence types: negation, SVO, imperative, causative,
                passive, emphatic, uvular, geminate...
```

---

## 🗂️ Repository Structure

```
amazigh-nlp-spacy/
│
├── notebooks/                           # Colab notebooks 01–04
├── data/
│   ├── tarifit_clitics.csv              # Clitic + lexicon dataset
│   └── tarifit_pbc_corpus.csv           # Phonetically balanced corpus
├── demo/
│   └── app.py                           # Streamlit app (Hugging Face Space)
├── models/                              # Trained spaCy models
│
├── advanced_morphology_tamazight.ipynb  # Notebook 05 — Tarifit morphology
├── tarifit_pbc_corpus.ipynb             # Notebook 06 — PBC corpus for TTS
├── NER_Amazigh_Phase_1_Data_Preprocessing.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📊 Languages supported

| Language | Model | Level |
|----------|-------|-------|
| Tamazight / Tarifit Berber | Custom (this project) | Native speaker annotations |
| Arabic | xx_ent_wiki_sm | Advanced |
| Spanish | es_core_news_lg | Native |
| French | fr_core_news_lg | Native |
| Catalan | ca_core_news_trf | Native |

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| spaCy 3.x | Tokenization, NER, morphology |
| scikit-learn | Sentiment classification (Naive Bayes + TF-IDF) |
| Python | Core language |
| Streamlit | Web interface |
| Hugging Face Spaces | Deployment |

---

## 🚀 Quick Start

```bash
git clone https://github.com/jamalinu/amazigh-nlp-spacy
cd amazigh-nlp-spacy
pip install -r requirements.txt
```

```python
import spacy
import joblib

# NER
nlp = spacy.load(".")
doc = nlp("Abdelkrim el Khattabi d amjahid n Arrif.")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Sentiment
modelo = joblib.load("modelo_tamazight.pkl")
print(modelo.predict(["Tamazight yelha, nefrah fell-as"]))
# Output: ['Positivo']
```

---

## 📈 Project Roadmap

- [x] Phase 1 — Data preprocessing and spaCy setup
- [x] Phase 2 — Advanced morphological tokenization
- [x] Phase 3 — Named Entity Recognition (NER)
- [x] Phase 4 — Sentiment analysis
- [x] Phase 5 — Tarifit clitic morphology analyzer
- [x] Phase 6 — Phonetically Balanced Corpus (57 sentences · 100% phoneme coverage)
- [ ] Phase 7 — Record audio with native speaker → first Tarifit TTS dataset
- [ ] Phase 8 — Train TTS model with Coqui TTS / VITS
- [ ] Phase 9 — Tifinagh script support ⵜⵉⴼⵉⵏⴰⵖ
- [ ] Phase 10 — Statistical model trained on annotated corpus

---

## 👤 Author

**Jamal Saghraoui** — Philologist & Computational Linguist

Native: Tamazight (Tarifit variant) · Arabic · Spanish · French · Catalan

> *"Bridging the gap between ancient languages and modern AI."*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jsaghraoui-blue?logo=linkedin)](https://www.linkedin.com/in/jsaghraoui/)
[![Hugging Face](https://img.shields.io/badge/🤗-jamalinu-orange)](https://huggingface.co/jamalinu)

---

*⵿ Tamazight · ⵜⴰⵔⵉⴼⵉⵜ · Tarifit — Low-resource NLP for Amazigh languages*
