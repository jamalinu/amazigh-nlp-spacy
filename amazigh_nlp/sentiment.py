import os
import joblib
from typing import List, Dict

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

STOPWORDS_TAMAZIGHT = {
    "d", "n", "i", "a", "ad", "ur", "ara", "deg", "ɣef", "s",
}

TRAIN_DATA = [
    ("Tamazight yelha, d tutlayt n yimaziɣen",  "Positivo"),
    ("Nefraḥ fell-as, d lxir i tmurt-nneɣ",     "Positivo"),
    ("Tafat tezga ɣef tmurt n yimaziɣen",        "Positivo"),
    ("Ur nessaram ara, aɣbel meqqren deg tmurt", "Negativo"),
    ("Ttmeggiḍ s wudem n tmurt, ur yelhi ara",   "Negativo"),
    ("Tamaziɣt ur tettwasexdem ara, d ɛib",      "Negativo"),
    ("Tamaziɣt d tutlayt n imaziɣen n Tamazɣa", "Neutral"),
    ("Agraw n tmaziɣt ad yili ass n sin",         "Neutral"),
    ("Taddart-a tesɛa 500 n yimezdaɣ imaziɣen",  "Neutral"),
]

class TamazightSentiment:
    EMOJI = {"Positivo": "😊", "Negativo": "😔", "Neutral": "😐"}

    def __init__(self, model_path=None):
        self.vectorizer = None
        self.model = None
        self.nlp = None
        if SPACY_AVAILABLE:
            try:
                self.nlp = spacy.load("xx_ent_wiki_sm")
            except OSError:
                pass
        if model_path and os.path.exists(model_path):
            saved = joblib.load(model_path)
            self.vectorizer = saved["vectorizer"]
            self.model = saved["model"]

    def clean(self, text):
        if self.nlp:
            doc = self.nlp(text.lower())
            tokens = [t.text for t in doc
                      if not t.is_punct
                      and t.text not in STOPWORDS_TAMAZIGHT
                      and len(t.text) > 1]
        else:
            tokens = [t for t in text.lower().split()
                      if t not in STOPWORDS_TAMAZIGHT and len(t) > 1]
        return " ".join(tokens)

    def train(self, train_data=None, save_path="models/sentiment_tamazight.pkl"):
        data = train_data or TRAIN_DATA
        texts = [self.clean(t) for t, _ in data]
        labels = [l for _, l in data]
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=0.3, random_state=42)
        self.vectorizer = TfidfVectorizer()
        X_train_vec = self.vectorizer.fit_transform(X_train)
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X_train_vec, y_train)
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        joblib.dump({"vectorizer": self.vectorizer, "model": self.model}, save_path)
        print(f"Model saved: {save_path}")

    def predict(self, text):
        if not self.model:
            raise RuntimeError("Call train() first.")
        vec = self.vectorizer.transform([self.clean(text)])
        label = self.model.predict(vec)[0]
        confidence = round(float(max(self.model.predict_proba(vec)[0])), 3)
        return {"label": label, "confidence": confidence}

    def print_result(self, text):
        result = self.predict(text)
        emoji = self.EMOJI.get(result["label"], "❓")
        print(f"\nTexto: {text}")
        print(f"{emoji} {result['label']} (confianza: {result['confidence']:.0%})")
