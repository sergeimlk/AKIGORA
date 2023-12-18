# departement_direction.py

# Importez les bibliothèques nécessaires
import pandas as pd
import plotly.express as px
import streamlit as st


def run(df):
    # Regrouper les données par secteurs et compter le nombre d'experts dans chaque secteur
    df_counts = df[df['type'] == 'expert'].groupby('sectors').size().reset_index(name='expertCount')

    # Chargement des données
    df = pd.read_csv(r'OneDrive/Documents/AKIGORA RAPPORT/DATA AKIGORA/AkiEXPERT.csv')

    # Regrouper les données de Paris, Paris Île-de-France, Paris et périphérique dans une seule catégorie "Paris"
    df['location_grouped'] = df['location'].replace({'Paris Île-de-France': 'Paris', 'Paris et périphérique': 'Paris'})

    # Créer une nouvelle colonne avec la catégorie "Autre" pour les villes avec une fréquence inférieure à 1%
    df['location_grouped'] = df['location_grouped'].where(df['location_grouped'].map(df['location_grouped'].value_counts(normalize=True)) >= 0.01, 'Autre')

    # Diagramme à secteurs pour % d'experts par ville avec la catégorie "Autre"
    fig1 = px.pie(df[df['type'] == 'expert'], names='location_grouped', title="% d'experts par ville")
    st.plotly_chart(fig1)

    # Supprimer la colonne temporaire
    df.drop('location_grouped', axis=1, inplace=True)

    # Indicateur 8: % d'experts par région avec la catégorie "Autre"
    fig2 = px.pie
    
    
    # Visualisation de la répartition des experts par domaine d'intervention (bar chart)
    st.subheader('Répartition des experts par domaine d\'intervention')  # Ajout d'un sous-titre
    # Utilisation des paramètres labels pour renommer les axes
    bar_chart = px.bar(df_counts, x='sectors', y='expertCount', title='Répartition des experts par domaine', labels={'sectors': 'Secteurs', 'expertCount': 'Nombre d\'experts'})
    st.plotly_chart(bar_chart)  # Affichage du graphique à barres

    