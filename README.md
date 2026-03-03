# 🌍 Amazigh/Berber NLP Pipeline with spaCy

> First open-source NLP pipeline for Tamazight (Amazigh/Berber language) 
> built by a native speaker with formal linguistics training.

## 🎯 Why this project matters

Tamazight is spoken by 30+ million people across North Africa, yet has 
virtually zero computational linguistics resources. This project addresses 
that gap by combining:

- Native speaker linguistic knowledge (Tamazight, Arabic, Spanish, French, Catalan)
- Formal philology and linguistics training
- Modern NLP tools (spaCy, Python)

## 🔬 What this project includes

| Module | Description | Status |
|--------|-------------|--------|
| Tokenizer | Custom Tamazight tokenizer | ✅ Done |
| NER | Named Entity Recognition (people, places) | ✅ Done |
| Morphology | Prefix/suffix analysis for Amazigh | 🔄 In progress |
| Corpus | Annotated sentences dataset | 🔄 In progress |

## 📊 Languages supported

| Language | Model | Level |
|----------|-------|-------|
| Tamazight/Berber | Custom (this project) | Native speaker annotations |
| Arabic | xx_ent_wiki_sm | Advanced |
| Spanish | es_core_news_lg | Native |
| French | fr_core_news_lg | Native |
| Catalan | ca_core_news_trf | Native |

🌍 Amazigh Entity Recognizer (AI)
This project uses Natural Language Processing (NLP) and Machine Learning to identify Names (PER) and Locations (LOC) in the Amazigh/Berber language.

🚀 Live Demo
Try the model here: [[PEGA AQUÍ TU ENLACE DE HUGGING FACE](https://huggingface.co/spaces/jamalinu/amazigh-nlp-demo)]

🛠️ Tech Stack
Framework: spaCy 3.x

Language: Python

Deployment: Hugging Face Spaces (Streamlit)

Dataset: Custom-built multilingual corpus (Berber/Arabic/Latin)

📈 Project Phases
Data Engineering: Conversion of raw text to DocBin format.

Training: Supervised learning with custom NER pipeline.

Deployment: Implementation of a web interface for real-time analysis.
## 📓 Project Roadmap & Notebooks

Este proyecto está estructurado en módulos progresivos para construir un pipeline completo de NLP para el Amazigh.

### 01. Foundations: Initial Setup & spaCy Basics
Introducción al entorno de trabajo y carga del modelo base multilingüe.
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/04_data_prep.ipynb)

### 02. Advanced Morphological Tokenization
Resolución de retos lingüísticos específicos del Amazigh: segmentación de clíticos y normalización de caracteres Tifinagh.
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/02_morfologia_avanzada.ipynb)

### 03. Named Entity Recognition (NER) for Tamazight
Identificación de topónimos (Rif) y personajes históricos en Latino y Tifinagh.
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/03_ner_amazigh.ipynb)
---

> **Note:** Si los enlaces de arriba no abren el archivo correcto, asegúrate de que los nombres de los archivos en tu carpeta `/notebooks` coincidan exactamente con los de los links.

## 🚀 Quick Start
```bash
git clone https://github.com/jamalinu/amazigh-nlp-spacy
pip install spacy
python -m spacy download es_core_news_lg
```
```python
import spacy
# Ver notebooks/ para ejemplos completos
```


## 👤 Author

**Jamal Saghraoui** — Philologist & Computational Linguist  
Native: Tamazight · Arabic · Spanish · French · Catalan  
[LinkedIn](https://www.linkedin.com/in/jsaghraoui/) | [Hugging Face](https://huggingface.co/jamalinu)
```



Ve a colab.research.google.com → nuevo notebook → renómbralo:

```
01_fundamentos_spacy_amazigh.ipynb
