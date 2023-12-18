import streamlit as st
import pandas as pd
import plotly.express as px
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_echarts

def run(df):
    # Chargement des données (remplissez le chemin du fichier CSV)
    df = pd.read_csv('DATA AKIGORA/AkiEXPERT.csv')

    # Visualisation : Répartition des experts par domaine d'intervention avec Plotly
    fig2 = px.pie(df, names='sectors', title="Répartition des experts par domaine d'intervention", labels={'sectors': 'Domaine d\'intervention'})
    fig2.update_layout(showlegend=True)  # Afficher la légende
    st.plotly_chart(fig2)

    # Visualisation : Répartition des experts par domaine d'intervention avec ECharts
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

    st_echarts(options=option, height="600px")
