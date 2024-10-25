# Importer les bibliothèques nécessaires
import streamlit as st
import langid
from transformers import pipeline
import os

# Classe pour la prédiction avec les modèles fine-tunés
class FineTunedHead:
    def __init__(self, model_name):
        self.pipe = pipeline('text-classification', model=model_name)

    def predict(self, text):
        return self.pipe(text)


# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define model paths relative to the script's directory
english_model_name = os.path.join(current_directory, "distilbert-base-uncased")
french_model_name = os.path.join(current_directory, "camembert-base")
arabe_model_name = os.path.join(current_directory, "bert-base-arabertv2")

english_model = FineTunedHead(english_model_name)
french_model = FineTunedHead(french_model_name)
arabe_model = FineTunedHead(arabe_model_name)

# Fonction pour détecter la langue
def detect_language(text):
    lang, _ = langid.classify(text)
    return lang

# Fonction de prédiction du sentiment
def predict_sentiment(text):
    lang = detect_language(text)

    if lang not in ["en", "fr", "ar"]:
        return None, None  # Si la langue n'est pas supportée

    try:
        if lang == "en":
            result = english_model.predict(text)
        elif lang == "fr":
            result = french_model.predict(text)
        elif lang == "ar":
            result = arabe_model.predict(text)

        sentiment_label = result[0]['label']
        probability = result[0]['score']
        
        # Conversion du label en texte humain
        sentiment = "positif" if sentiment_label == "LABEL_1" else "négatif"
        return sentiment, probability

    except Exception as e:
        return None, None

# Interface utilisateur avec Streamlit
st.title("Analyse de Sentiment Multilingue")

# Zone de saisie pour le texte
text_input = st.text_area("Entrez votre texte ici")

# Si l'utilisateur appuie sur le bouton ou entre du texte
button_clicked = st.button("Analyser")

# Analyser automatiquement si du texte est entré ou si le bouton est cliqué
if text_input or button_clicked:  # Si du texte est saisi ou le bouton est cliqué
    sentiment, probability = predict_sentiment(text_input)

    if sentiment is not None and probability is not None:
        # Affiche le résultat avec la probabilité correctement formatée
        st.success(f"Sentiment prédit : {sentiment} avec probabilité {probability:.4f}")
    else:
        st.error("Erreur lors de la prédiction ou langue non supportée.")
