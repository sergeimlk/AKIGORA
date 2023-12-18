import streamlit as st
from streamlit_echarts import st_echarts

def run(df):
    # Votre code pour la page de remerciements avec l'utilisation de df si nécessaire
    st.title("MERCI!")  # Ajouter un color picker pour choisir la couleur du texte
    selected_color = st.color_picker("Choisissez la couleur du texte", "#FF0000")  # Couleur par défaut : rouge

    data = [
        {"name": name, "value": value}
        for name, value in [
              ("   DATA VISUALIZATION   ", "999"),
            ("   DASHBOARD INTERACTIF   ", "888"),
            ("   INDICATEURS DE DONNÉES   ", "777"),
            ("   ÉVOLUTION DES DONNÉES   ", "688"),
            ("   INSCRIPTIONS   ", "588"),
            ("   DONNÉES FINANCIÈRES   ", "516"),
            ("   STREAMLIT DASHBOARD   ", "515"),
            ("   CONCEPTION   ", "483"),
            ("   DÉVELOPPEMENT   ", "462"),
            ("   VISUALISATION CLAIRE   ", "449"),
            ("   PROJET   ", "407"),
            ("   ÉTUDIANTS   ", "406"),
            ("   IA MICROSOFT   ", "386"),
            ("   BAYONNE   ", "385"),
            ("   ANALYSTE DE DONNÉES   ", "375"),
            ("   DÉVELOPPEUR EN IA   ", "355"),
            ("   FORMATION   ", "355"),
            ("   SIMPLON   ", "335"),
            ("   ÉCOLE MICROSOFT IA   ", "324"),
            ("   REMERCIEMENTS   ", "300"),
            ("   RAPPORT   ", "280"),
            ("   AKIGORA   ", "270"),
            ("   STREAMLIT APP   ", "260"),
            ("   VISUALISATION DE DONNÉES   ", "250"),
            ("   GRAPHIQUES INTERACTIFS   ", "240"),
            ("   TABLEAUX DE BORD   ", "230"),
            ("   DATA SCIENCE   ", "220"),
            ("   ANALYSE DE DONNÉES   ", "210"),
            ("   PROGRAMMATION   ", "200"),
            ("   CODING   ", "190"),
            ("   PYTHON   ", "180"),
            ("   PROGRAMMEUR   ", "170"),
            ("   TECHNOLOGIE   ", "160"),
            ("   INTELLIGENCE ARTIFICIELLE   ", "150"),
            ("   MACHINE LEARNING   ", "140"),
            ("   STATISTIQUES   ", "130"),
            ("   BIG DATA   ", "120"),
            ("   VISUALISATION GRAPHIQUE   ", "110"),
            ("   CODAGE EN PYTHON   ", "100"),
            ("   AKIGORA TEAM   ", "90"),
            ("   STREAMLIT.COM   ", "70"),
            ("   DATA ANALYST   ", "60"),
            ("   DAX   ", "50"),
        ]
    ]

    wordcloud_option = {
        "series": [{
            "type": "wordCloud",
            "data": data,
            "textStyle": {
                "fontSize": 80,
                "color": selected_color,  # Utiliser la couleur choisie par l'utilisateur
                "fontWeight": "bold",
                "opacity": 0.7,
                "rotate": {"random": "horizontal"},
            },
            "animation": True,
            "animationDuration": 2000,
            "animationEasingUpdate": "cubicInOut",
        }],
        "backgroundColor": "rgba(0, 0, 0, 0)"
    }

    st_echarts(wordcloud_option)
