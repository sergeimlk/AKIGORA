import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
from PIL import Image  

# Définir le titre de la page et l'état initial de la barre latérale
st.set_page_config(page_title="AKIGORA DASHBOARD", layout="wide", initial_sidebar_state="collapsed")


# Ajouter le logo dans la barre latérale et réduire la taille de 30%
logo_path = r"AKIGORA/DATA AKIGORA/2LOGO.PNG"
logo = Image.open(logo_path)
logo_resized = logo.resize((int(logo.width * 1), int(logo.height * 1)))  # Réduire de 30%
st.sidebar.image(logo_resized, use_column_width=True)

import contexte_projet
import departement_rh
import MAP
import departement_direction
import departement_marketing
import departement_technique
import remerciements

# Charger les données
#df = pd.read_csv(r'OneDrive/Documents/AKIGORA RAPPORT/DATA AKIGORA/AkiEXPERT.csv')
df = pd.read_csv(r'AKIGORA/DATA AKIGORA/AkiEXPERT.csv')

st.sidebar.title("📊 AKIGORA DASHBOARD")

pages = ["🚀Contexte du projet", "👥Département RH", "🗺️Carte", "🎯Département Direction", "📢Département Marketing", "🔧Les Experts par Domaine", "🙏Remerciements"]
page = st.sidebar.radio("🔬Analyse de données:", pages)

# Exécuter le code correspondant à la page sélectionnée
if page == pages[0]:
    contexte_projet.run()
elif page == pages[1]:
    departement_rh.run(df)
elif page == pages[2]:
    MAP.run()
elif page == pages[3]:
    departement_direction.run(df)
elif page == pages[4]:
    departement_marketing.run(df)
elif page == pages[5]:
    departement_technique.run(df)
elif page == pages[6]:
    remerciements.run(df)
    
    
