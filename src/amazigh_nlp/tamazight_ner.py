import spacy
from spacy import displacy
from typing import List, Dict

PATTERNS_LATIN = [
    {"label": "LOC", "pattern": "Tamazgha"},
    {"label": "LOC", "pattern": "Agadir"},
    {"label": "LOC", "pattern": "Nador"},
    {"label": "LOC", "pattern": "Alhucima"},
    {"label": "LOC", "pattern": "Arrif"},
    {"label": "LOC", "pattern": "Tizi Wezzu"},
    {"label": "LOC", "pattern": "Bgayet"},
    {"label": "LOC", "pattern": "Lezzayer"},
    {"label": "PER", "pattern": "Massinissa"},
    {"label": "PER", "pattern": "Jugurtha"},
    {"label": "PER", "pattern": "Dihya"},
    {"label": "PER", "pattern": "Tacfarinas"},
    {"label": "PER", "pattern": "Abdelkrim"},
    {"label": "PER", "pattern": "Abdelkrim el Khattabi"},
    {"label": "ORG", "pattern": "IRCAM"},
    {"label": "ORG", "pattern": "HCA"},
]

PATTERNS_TIFINAGH = [
    {"label": "LOC", "pattern": "ⵍⵃⵓⵙⵉⵎⴰ"},
    {"label": "LOC", "pattern": "ⴰⵣⵖⴰⵏⵖⴰⵏ"},
    {"label": "LOC", "pattern": "ⴰⵔⵔⵉⴼ"},
    {"label": "LOC", "pattern": "ⵜⴰⵎⴰⵣⵖⴰ"},
    {"label": "PER", "pattern": "ⵎⴰⵙⵉⵏⵉⵙⴰ"},
    {"label": "PER", "pattern": "ⵜⵉⵀⵢⴰ"},
]

class TamazightNER:
    LABEL_NAMES = {"PER": "Person", "LOC": "Location", "ORG": "Organization"}

    def __init__(self, custom_patterns=None):
        self.nlp = spacy.blank("xx")
        self.ruler = self.nlp.add_pipe("entity_ruler")
        all_patterns = PATTERNS_LATIN + PATTERNS_TIFINAGH
        if custom_patterns:
            all_patterns += custom_patterns
        self.ruler.add_patterns(all_patterns)

    def predict(self, text):
        doc = self.nlp(text)
        return [
            {
                "text":       ent.text,
                "label":      ent.label_,
                "label_name": self.LABEL_NAMES.get(ent.label_, ent.label_),
                "start":      ent.start_char,
                "end":        ent.end_char,
            }
            for ent in doc.ents
        ]

    def visualize(self, text, jupyter=True):
        doc = self.nlp(text)
        displacy.render(doc, style="ent", jupyter=jupyter)

    def print_entities(self, text):
        entities = self.predict(text)
        print(f"\nText: {text}")
        if entities:
            for ent in entities:
                print(f"  [{ent['label_name']}] '{ent['text']}'")
        else:
            print("  (no entities detected)")
