# contexte_projet.py
import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image

def run():
    st.title("STAGE AKIGORA🚀")

    # Créer deux colonnes
    col_texte, col_logo = st.columns([2, 1])  # 2/3 pour le texte, 1/3 pour le logo

    col_texte.subheader("🔍 Analyse de données par SIMPLON")
    col_texte.subheader("🎓 École Microsoft IA by SIMPLON")
    col_texte.subheader(" 👩‍💻 Data Analyst & Développeur en Intelligence Artificielle")
    col_texte.write("Ce projet s'inscrit dans le cadre de la formation Data Analyst et Développeur en Intelligence Artificielle à l'École IA Microsoft by SIMPLON à Bayonne.")
    col_texte.write("\n")
    col_texte.subheader("🌐 LE CONTEXTE ET LE PROJET")
    col_texte.write("Le projet de Data Visualization vise à permettre à un groupe d'étudiants de créer un dashboard interactif pour visualiser divers indicateurs. Ces indicateurs sont disponibles aujourd’hui grâce aux données que nous exploitons en interne. Nous manquons aujourd’hui d’un outil pour nous permettre d’observer l’évolution de nos données dans le temps. Ces données sont de types variables, il peut s’agir de données sur les inscriptions, de données financières, de données sur l’utilisation de la plateforme, etc.")
    col_texte.write("Le projet consiste à concevoir et développer un dashboard interactif qui offre une visualisation claire et efficace des indicateurs de données sélectionnés et communiqués aux étudiants.")
    col_texte.write("\n")

    # Colonne du logo à droite
    logo_path = "OneDrive/Documents/AKIGORA RAPPORT/DATA AKIGORA/SIMP.png"
    logo = Image.open(logo_path)
    col_logo.image(logo, use_column_width=True, caption="")

    # Graphique liquidFill sous les deux colonnes
    liquidfill_option = {
        "series": [{"type": "liquidFill", "data": [0.1, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1], "itemStyle": {"color": "red"}}],
        "backgroundColor": "transparent"  # Cette ligne rend l'arrière-plan transparent
    }
    st_echarts(liquidfill_option)

if __name__ == "__main__":
    run()