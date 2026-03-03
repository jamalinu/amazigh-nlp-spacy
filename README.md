# 🌍 Amazigh/Berber NLP Pipeline with spaCy
> First open-source NLP pipeline for Tamazight (Amazigh/Berber language)  
> built by a native speaker with formal linguistics training.

## 🎯 Why this project matters
Tamazight is spoken by 30+ million people across North Africa, yet has 
virtually zero computational linguistics resources. This project addresses 
that gap by combining:
- Native speaker linguistic knowledge (Tamazight, Arabic, Spanish, French, Catalan)
- Formal philology and linguistics training
- Modern NLP tools (spaCy, scikit-learn, Python)

## 🔬 What this project includes

| Module | Description | Status |
|--------|-------------|--------|
| Tokenizer | Custom Tamazight tokenizer | ✅ Done |
| NER | Named Entity Recognition (people, places) | ✅ Done |
| Sentiment Analysis | Positive / Negative / Neutral classifier | ✅ Done |
| Morphology | Prefix/suffix analysis for Amazigh | 🔄 In progress |
| Corpus | Annotated sentences dataset | 🔄 In progress |

## 🚀 Live Demo
Try the model here: [amazigh-nlp-demo on Hugging Face](https://huggingface.co/spaces/jamalinu/amazigh-nlp-demo)

The demo includes:
- 🏷️ **Named Entity Recognizer** — detects people (PER) and locations (LOC)
- 🎭 **Sentiment Analyzer** — classifies comments as Positive, Negative or Neutral

## 📊 Languages supported

| Language | Model | Level |
|----------|-------|-------|
| Tamazight/Berber | Custom (this project) | Native speaker annotations |
| Arabic | xx_ent_wiki_sm | Advanced |
| Spanish | es_core_news_lg | Native |
| French | fr_core_news_lg | Native |
| Catalan | ca_core_news_trf | Native |

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| spaCy 3.x | Tokenization, NER, preprocessing |
| scikit-learn | Sentiment classification (Naive Bayes + TF-IDF) |
| Python | Core language |
| Streamlit | Web interface |
| Hugging Face Spaces | Deployment |

## 📈 Project Phases

1. **Data Engineering** — Conversion of raw text to DocBin format
2. **NER Training** — Supervised learning with custom NER pipeline
3. **Sentiment Analysis** — TF-IDF + Naive Bayes classifier for social comments
4. **Deployment** — Live web interface for real-time analysis

## 📓 Project Roadmap & Notebooks

### 01. Foundations: Initial Setup & spaCy Basics
Introduction to the working environment and loading the multilingual base model.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/01_fundamentos_spacy_amazigh.ipynb)

### 02. Advanced Morphological Tokenization
Solving Amazigh-specific linguistic challenges: clitic segmentation and Tifinagh character normalization.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/02_morfologia_avanzada.ipynb)

### 03. Named Entity Recognition (NER) for Tamazight
Identification of toponyms (Rif) and historical figures in Latin and Tifinagh scripts.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/03_ner_amazigh.ipynb)

### 04. Sentiment Analysis — Tamazight Social Comments
First sentiment classifier for Tamazight. Labels: Positive / Negative / Neutral.  
Built with TF-IDF + Naive Bayes and a custom Tamazight sentiment lexicon.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/04_sentiment_tamazight.ipynb)

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

# Sentiment
modelo = joblib.load("modelo_tamazight.pkl")
print(modelo.predict(["Tamazight yelha, nefraḥ fell-as"]))
# → ['Positivo']
```

## 👤 Author
**Jamal Saghraoui** — Philologist & Computational Linguist  
Native: Tamazight · Arabic · Spanish · French · Catalan

> *"Bridging the gap between ancient languages and modern AI."*

[LinkedIn](https://www.linkedin.com/in/jsaghraoui/) | [Hugging Face](https://huggingface.co/jamalinu)
