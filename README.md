# 🌍 Amazigh/Berber NLP Pipeline with spaCy
> First open-source NLP pipeline for Tamazight (Amazigh/Berber language)  
> built by a native speaker with formal linguistics training.

## 🎯 Why this project matters
Tamazight is spoken by **30+ million people** across North Africa, yet has 
virtually zero computational linguistics resources. This project addresses 
that gap by combining:
- Native speaker linguistic knowledge (Tamazight, Arabic, Spanish, French, Catalan)
- Formal philology and linguistics training
- Modern NLP tools (spaCy, scikit-learn, Python)

---

## 🚀 Live Demo
**👉 [Try it here — amazigh-nlp-demo on Hugging Face](https://huggingface.co/spaces/jamalinu/amazigh-nlp-demo)**

The demo includes three tools running live:

| Tool | Description |
|------|-------------|
| 🔎 Named Entity Recognizer | Detects people (PER) and locations (LOC) |
| 🎭 Sentiment Analyzer | Classifies comments as Positive / Negative / Neutral with confidence % |
| 🏔️ Tarifit Morphology Analyzer | POS tagging, clitic tokenization and morpheme segmentation |
| 🎙️ TTS Text Normalizer | Converts informal Tarifit (Chat-Arabic numerals, digraphs) to phonetic symbols |

---

## 🔬 Project Modules

| # | Module | Description | Status |
|---|--------|-------------|--------|
| 01 | Tokenizer | Custom Tamazight tokenizer with clitic handling | ✅ Done |
| 02 | NER Data Prep | DocBin annotation pipeline | ✅ Done |
| 03 | NER Training | Supervised NER model (100% F1) | ✅ Done |
| 04 | Sentiment Analysis | Positive / Negative / Neutral classifier | ✅ Done |
| 05 | TTS Corpus | Phonetically Balanced Corpus for Tarifit TTS | ✅ Done |
| 06 | Morphology | Full morphological pipeline for Tarifit | ✅ Done |
| 07 | TTS Frontend | Linguistic text normalization for Tarifit TTS | ✅ Done |
| 08 | Corpus | Annotated sentences dataset | 🔄 In progress |

---

## 📓 Notebooks

### 01. Custom NLP Pipeline for Low-Resource Languages
Builds a spaCy tokenizer from scratch for Tamazight.
Handles clitic segmentation and Tifinagh character normalization.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/Building_Custom_NLP_Pipelines_for_Low_Resource_Languages_The_Case_of_Amazigh.ipynb)

---

### 02. NER Data Preprocessing — DocBin Format
Converts manually annotated Amazigh sentences into spaCy's binary format (DocBin).
Supports both Latin and Tifinagh scripts.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/NER_Amazigh_Phase_1_Data_Preprocessing.ipynb)

---

### 03. NER Model Training & Evaluation
Trains a custom spaCy NER model for Amazigh from scratch.
Reaches **100% F1-score** on training data.
Exports the final model as `model-best`.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/NER_Amazigh_Phase_2_Model_Training_%26_Evaluation.ipynb)

---

### 04. Tamazight Social Sentiment Analyzer
First sentiment classifier for Tamazight social media comments.
Labels: **Positive / Negative / Neutral**.

Key features:
- **90 native-validated sentences** (30 per category) — everyday life in the Rif
- **Tarifit sentiment lexicon** — covers both Tarifit colloquial and classical Tamazight
- **BOW + lexicon features** combined for better generalization
- **Cross-validation (5-fold)** for reliable evaluation
- Best model: **SVM 88.9%** accuracy

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/Tamazight_Social_Sentiment_Analyzer.ipynb)

---

### 05. Tarifit Phonetically Balanced Corpus (TTS)
**First TTS corpus for Tarifit (Riffian Berber).**
57 sentences with manual IPA transcription covering **100% of the Tarifit phoneme inventory**.
Exported in Coqui TTS / VITS format. Ready for voice synthesis.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/Tarifit_PBC_Corpus.ipynb)

---

### 06. Advanced Morphology — Tarifit NLP
Full morphological pipeline for Tarifit Berber:
- Custom clitic tokenizer (proclitics + enclitics)
- Rule-based POS tagger with lexicon + morphological patterns
- Morpheme segmenter (prefix · root · suffix)
- Consonantal root extractor
- Visualized with displaCy

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/advanced_morphology_tamazight.ipynb)

---

### 07. Tarifit TTS — Linguistic Frontend (End-to-End Pipeline)
Complete text normalization pipeline for Tarifit and Tashelhit TTS training.

Key features:
- **Multi-script normalization**: Chat-Arabic numerals (`7→ħ`, `9→q`, `3→ʕ`), digraphs (`gh→ɣ`, `sh→ʃ`, `dh→dˁ`), linguistic diacritics (`ṣ→sˁ`, `ẓ→zˁ`, `ḍ→dˁ`, `ṭ→tˁ`)
- **Tifinagh → Latin → Phonetic** full transliteration pipeline (IRCAM standard)
- **Tashelhit phoneme inventory** — 29 phonemes documented and validated
- **Customer service corpus** — 24 native Tarifit sentences **validated by a native speaker** with **100% phoneme coverage**
- Exports production-ready `metadata.csv` in Coqui TTS / VITS format

**Pipeline:**
```
Tifinagh (IRCAM) ─┐
Latin informal   ─┼→ Normalizer → Phonetic symbols → metadata.csv → Neural vocoder
Chat-Arabic      ─┘
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/Tarifit_TTS_Linguistic_Frontend.ipynb)

---

## 📊 Languages supported

| Language | Model | Level |
|----------|-------|-------|
| Tamazight/Berber | Custom (this project) | Native speaker annotations |
| Arabic | xx_ent_wiki_sm | Advanced |
| Spanish | es_core_news_lg | Native |
| French | fr_core_news_lg | Native |
| Catalan | ca_core_news_trf | Native |

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| spaCy 3.x | Tokenization, NER, morphological analysis |
| scikit-learn | Sentiment classification (SVM + BOW + Lexicon) |
| Python | Core language |
| Streamlit | Web interface |
| Hugging Face Spaces | Deployment |
| displaCy | Linguistic visualization |

---

## 🚀 Quick Start

```bash
git clone https://github.com/jamalinu/amazigh-nlp-spacy
pip install spacy scikit-learn streamlit joblib
python -m spacy download xx_ent_wiki_sm
```

```python
import spacy
import joblib

# NER
nlp = spacy.load(".")
doc = nlp("Abdelkrim el Khattabi d amjahid n Arrif.")
for ent in doc.ents:
    print(ent.text, ent.label_)
# → Abdelkrim el Khattabi PER
# → Arrif LOC

# Sentiment
modelo = joblib.load("modelo_tarifit_sentiment.pkl")
print(modelo.predict(["Said ynje7 di lemti7an"]))
# → ['Positivo']
```

---

## 📈 Results

| Module | Metric | Score |
|--------|--------|-------|
| NER | F1-score | 100% (training set) |
| Sentiment | Accuracy | **88.9%** (90 native sentences, CV-5) |
| TTS Corpus | Phoneme coverage | 100% (27 phonemes) |
| TTS Frontend | Normalization rules | Chat-Arabic + digraphs + diacritics + Tifinagh |
| TTS Customer Service Corpus | Phoneme coverage | 100% (24 native-validated sentences) |
| Morphology | Rules coverage | Tarifit core grammar |

---

## 👤 Author
**Jamal Saghraoui** — Philologist & Computational Linguist  
Native: Tamazight · Arabic · Spanish · French · Catalan

> *"Bridging the gap between ancient languages and modern AI."*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/jsaghraoui/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-yellow?logo=huggingface)](https://huggingface.co/jamalinu)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/jamalinu)
