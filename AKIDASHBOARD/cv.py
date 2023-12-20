import streamlit as st
import pandas as pd

def run():
    # Charger le DataFrame
    df = pd.read_png('AKIGORA/DATA AKIGORA/CV.png')

# Vérifiez si le script est exécuté directement (non importé en tant que module)
if __name__ == "__main__":
    run()
