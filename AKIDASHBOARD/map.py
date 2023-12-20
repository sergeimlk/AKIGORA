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
            lat, lon = geo_data['location']['coordinates']  # Note le changement de lat et long à lat et lon
            return lat, lon
        except:
            return None, None

    # Appliquer la fonction à chaque ligne du DataFrame
    df[['latitude', 'longitude']] = df['geo'].apply(extract_coordinates).apply(pd.Series)

    # Inverser latitude et longitude
    df[['latitude', 'longitude']] = df[['longitude', 'latitude']]

    # Afficher le DataFrame résultant
    st.dataframe(df[['latitude', 'longitude']])

    # Données pour les nouvelles couches
    chart_data = df[['latitude', 'longitude']]

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
            # Couche HexagonLayer
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position='[longitude, latitude]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            # Couche ScatterplotLayer
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

# Vérifiez si le script est exécuté directement (non importé en tant que module)
if __name__ == "__main__":
    run()
