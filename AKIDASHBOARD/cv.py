import streamlit as st
import pandas as pd

def run():
    # Charger le DataFrame (image)
    df = pd.read_png(r'AKIGORA/DATA AKIGORA/CV.png')

    # Afficher l'image
    st.image(df)

# Vérifiez si le script est exécuté directement (non importé en tant que module)
if __name__ == "__main__":
    run()
