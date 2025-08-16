import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

# Coordinates for West Lafayette, IN
LAT, LON = 40.4259, -86.9081

st.set_page_config(page_title = "Air Quality Tracker ", layout="wide")
st.title("🌬 Live Air Quality Tracker – West Lafayette")
st.write("Real-time AQI and pollutant levels fetched from OpenWeatherMap.")


url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    aqi = data["list"][0]["main"]["aqi"]
    components = data["list"][0]["components"]
    aqi_map = {
        1: "Good 😊",
        2: "Fair 🙂",
        3: "Moderate 😐",
        4: "Poor 😷",
        5: "Very Poor 🤢"
    }
    st.subheader(f"AQI Index: {aqi} – {aqi_map.get(aqi, 'Unknown')}")
    df = pd.DataFrame(components.items(), columns=["Pollutant", "Concentration (µg/m³)"])
    st.write("### Pollutant Levels")
    st.dataframe(df)
    fig = px.bar(df, x="Pollutant", y="Concentration (µg/m³)",
                 title="Pollutant Concentrations", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"Failed to fetch data: {response.status_code}")




