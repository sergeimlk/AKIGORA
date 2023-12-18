import streamlit as st
import pandas as pd
import plotly.express as px

def run(df):
    
    # Conversion de la colonne 'createdAt' en format datetime
    df['createdAt'] = pd.to_datetime(df['createdAt'], format="%d/%m/%Y", errors='coerce')

    # Calcul du nombre cumulatif d'experts inscrits au fil du temps
    cumulative_experts = df.groupby('createdAt').size().cumsum().reset_index()

    # Visualisation : Evolution du nombre d'experts inscrits sur la plateforme au fil du temps
    line_chart = px.line(cumulative_experts, x='createdAt', y=0, title="Évolution du nombre d'experts inscrits sur la plateforme au fil du temps")
    line_chart.update_layout(xaxis_title='Date de création', yaxis_title="Nombre d'experts inscrits")
    
    st.subheader('Évolution du nombre d\'experts inscrits sur la plateforme au fil du temps')  # Ajout d'un sous-titre
    st.plotly_chart(line_chart)  # Affichage du graphique en ligne
    
    
        # Visualisation de la répartition des experts par domaine d'intervention (bar chart)
    st.subheader('Répartition des experts par domaine d\'intervention')  # Ajout d'un sous-titre
    # Calculer le nombre d'experts par secteur
    df_counts = df['sectors'].value_counts().reset_index()
    df_counts.columns = ['sectors', 'expertCount']

    # Utilisation des paramètres labels pour renommer les axes
    bar_chart = px.bar(df_counts, x='sectors', y='expertCount', title='Répartition des experts par domaine', color='sectors', color_discrete_map={'sectors': 'red'})
    st.plotly_chart(bar_chart)  # Affichage du graphique à barres

