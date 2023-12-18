import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_echarts import st_echarts  # Ajout de l'import pour st_echarts

def run(df):
    # Votre code existant pour compter les experts par secteur
    sector_counts = df['sectors'].value_counts()
    df_counts = pd.DataFrame({'sectors': sector_counts.index, 'expertCount': sector_counts.values})

    
    
    
    # Visualisation de la répartition des experts par domaine d'intervention (bar chart)
    st.subheader('Répartition des experts par domaine d\'intervention')  # Ajout d'un sous-titre
    # Utilisation des paramètres labels pour renommer les axes
    bar_chart = px.bar(df_counts, x='sectors', y='expertCount', title='Répartition des experts par domaine', labels={'sectors': 'Secteurs', 'expertCount': 'Nombre d\'experts'})
    st.plotly_chart(bar_chart)  # Affichage du graphique à barres

    
    
    # Ajout de la Répartition des experts par domaine d'intervention avec ECharts (pie chart)
    st.subheader('Répartition des experts par domaine d\'intervention avec ECharts')  # Ajout d'un sous-titre
    option = {
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "Domaine d'intervention",
                "type": "pie",
                "radius": [50, 250],
                "center": ["50%", "50%"],
                "roseType": "area",
                "itemStyle": {"borderRadius": 8},
                "data": [
                    {"value": count, "name": sector}
                    for sector, count in df['sectors'].value_counts().items()
                ],
            }
        ],
    }

    st_echarts(options=option, height="600px")  # Affichage du graphique à secteurs avec ECharts
    
    
    
    