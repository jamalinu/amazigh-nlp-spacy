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

## 📓 Project Roadmap & Notebooks

Este proyecto está estructurado en módulos progresivos para construir un pipeline completo de NLP para el Amazigh.

### 01. Foundations: Initial Setup & spaCy Basics
Introducción al entorno de trabajo y carga del modelo base multilingüe.
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/01_foundations_spacy.ipynb)

### 02. Advanced Morphological Tokenization
Resolución de retos lingüísticos específicos del Amazigh: segmentación de clíticos y normalización de caracteres Tifinagh.
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jamalinu/amazigh-nlp-spacy/blob/main/notebooks/02_morfologia_avanzada.ipynb)

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

## 📓 Notebooks

1. `01_fundamentos.ipynb` — spaCy basics + morphological analysis
2. `02_comparativa.ipynb` — Cross-lingual analysis ES/FR/CA/AR
3. `03_bereber_pipeline.ipynb` — Tamazight NER training ⭐

## 👤 Author

**Tu Nombre** — Philologist & Computational Linguist  
Native: Tamazight · Arabic · Spanish · French · Catalan  
[LinkedIn](#) | [Hugging Face](#)
```

---

## Bloque 3 — Tu primer notebook subido *(1 hora)*

### Abre Google Colab ahora mismo

Ve a colab.research.google.com → nuevo notebook → renómbralo:

```
01_fundamentos_spacy_amazigh.ipynb
