import streamlit as st
import pandas as pd
import pydeck as pdk
import json

def run():
    # Charger le DataFrame
    df = pd.read_csv('DATA AKIGORA/AkiEXPERT.csv')

    # Fonction pour extraire les coordonnées
    def extract_coordinates(geo):
        try:
            geo_data = json.loads(geo)
            lat, long = geo_data['location']['coordinates']
            return lat, long
        except:
            return None, None

    # Appliquer la fonction à chaque ligne du DataFrame
    df[['latitude', 'longitude']] = df['geo'].apply(extract_coordinates).apply(pd.Series)

    # Inverser latitude et longitude
    df[['latitude', 'longitude']] = df[['longitude', 'latitude']]

    st.title("🗺️LOCALISATION DES EXPERTS🛑")

    # Afficher le DataFrame résultant
    #st.dataframe(df[['latitude', 'longitude']])

    # Afficher la carte avec Pydeck
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v11",
        initial_view_state=pdk.ViewState(
            latitude=df['latitude'].mean(),
            longitude=df['longitude'].mean(),
            zoom=5,
            pitch=50,
        ),
        layers=[
            # HexagonLayer pour une visualisation en bâtons hexagonaux 3D
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[longitude, latitude]',
                radius=20000,
                elevation_scale=150,
                elevation_range=[0, 10000],
                pickable=True,
                extruded=True,
                get_fill_color="[255, 165, 0]",  # Couleur orange en format RGB
            ),
        ],
    )),
            # ScatterplotLayer for individual data points
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_radius=10000,
                get_color='[200, 3, 0, 160]',
                get_elevation='quantity',
                pickable=True,
            ),
        ],
    ))

# Vérifiez si le script est exécuté directement (non importé en tant que module)
if __name__ == "__main__":
    run()
