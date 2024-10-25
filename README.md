# Multilingual Sentiment Analysis

Ce projet est un modèle d'analyse des sentiments capable de détecter et de classer des sentiments en trois langues : anglais, français, et arabe. Pour ce faire, trois modèles ont été créés, chacun optimisé pour une langue spécifique, en utilisant plusieurs algorithmes de machine learning (ML) et deep learning (DL), ainsi que des modèles pré-entraînés.

## Aperçu du projet

L’objectif de ce projet est d'analyser le sentiment d’un texte en fonction de sa langue, en identifiant s’il est positif ou négatif. Voici le schéma général de l’architecture du projet :

                      ┌────────────────────────────────────────────────────────────┐
                      │          Multilingual Sentiment Model                      │
                      │ (Language Detection and Fine-Tuned Transformers for        │
                      │  English, French, and Arabic Sentiment Analysis)           │
                      └────────────────────────────────────────────────────────────┘
                                                  │                    
                                                  │                    
                         ┌────────────────────────┴─────────────────────────┐          
                         │                         │                         │          
              ┌──────────┴─────────┐     ┌─────────┴──────────┐      ┌────────┴─────────┐     
              │ Sentiment Head      │     │ Sentiment Head     │      │ Sentiment Head  │     
              │ (English)           │     │ (French)          │      │ (Arabic)        │     
              │ Fine-tuned on       │     │ Fine-tuned on     │      │ Fine-tuned on   │     
              │ English Data        │     │ French Data       │      │ Arabic Data     │     
              └─────────────────────┘     └───────────────────┘      └─────────────────┘     
                         │                         │                         │
                  Output (English)           Output (French)             Output (Arabic)


## Fonctionnalités

1. **Détection de la langue** : Utilisation de `langid` pour détecter si le texte est en anglais, en français ou en arabe.
2. **Modèles fine-tunés pour chaque langue** :
   - **Anglais** : Utilise un modèle DistilBERT.
   - **Français** : Utilise CamemBERT.
   - **Arabe** : Utilise ArabERT.
3. **Prédiction des sentiments** : 
   - Après la détection de la langue, le texte est envoyé au modèle spécifique pour effectuer la classification des sentiments (positif ou négatif).
   - Les labels de sortie (`LABEL_1` pour positif, `LABEL_0` pour négatif) sont convertis en des étiquettes lisibles (`positif` ou `négatif`) avec une probabilité associée.

## Algorithmes Utilisés

Ce projet utilise plusieurs approches ML et DL, notamment :
- **Algorithmes ML** : XGBClassifier, LinearRegression, MultinomialNB
- **Algorithmes DL** : Réseaux de neurones artificiels (ANN), LSTM, GRU, FastText

Chaque modèle a été entraîné et fine-tuné pour chaque langue à l’aide de [Hugging Face Transformers](https://huggingface.co/transformers/).
