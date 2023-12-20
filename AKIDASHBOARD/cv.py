import streamlit as st
import pandas as pd
import pydeck as pdk
import json

def run():
    # Charger le DataFrame
    df = pd.read_pdf('AKIGORA/DATA AKIGORA/CV.pdf')

# Vérifiez si le script est exécuté directement (non importé en tant que module)
if __name__ == "__main__":
    run()
