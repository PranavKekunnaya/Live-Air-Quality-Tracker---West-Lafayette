# 🌬 Live Air Quality Tracker – West Lafayette

A Streamlit dashboard that fetches **real-time air quality data** from the **OpenWeatherMap API**, displays AQI ratings, pollutant concentrations, and interactive charts. Built with Python, Pandas, and Plotly for clear, visual monitoring of air quality in West Lafayette, IN.

---

## 📊 Features

- Fetch live **AQI** (Air Quality Index) and pollutant levels (SO₂, NO₂, PM10, PM2.5, O₃, CO)  
- Display **qualitative AQI categories**: Good, Fair, Moderate, Poor, Very Poor  
- Interactive **bar chart** visualization of pollutant concentrations  
- Easy-to-run **Streamlit dashboard**

---

## 🔗 AQI Categories

| Qualitative Name | Index | SO₂ | NO₂ | PM10 | PM2.5 | O₃ | CO |
|-----------------|-------|-----|-----|------|-------|----|----|
| Good            | 1     | 0–20 | 0–40 | 0–20 | 0–10 | 0–60 | 0–4400 |
| Fair            | 2     | 20–80 | 40–70 | 20–50 | 10–25 | 60–100 | 4400–9400 |
| Moderate        | 3     | 80–250 | 70–150 | 50–100 | 25–50 | 100–140 | 9400–12400 |
| Poor            | 4     | 250–350 | 150–200 | 100–200 | 50–75 | 140–180 | 12400–15400 |
| Very Poor       | 5     | ≥350 | ≥200 | ≥200 | ≥75 | ≥180 | ≥15400 |

---

## 🚀 Installation

1. **Install dependencies**
```bash
pip install -r requirements.txt
Add your OpenWeatherMap API key

Option 1: Replace YOUR_API_KEY directly in app.py

Option 2 (recommended): Create a .env file in the project folder with:

text
Copy
Edit
API_KEY=your_api_key_here

---

## 🏃 Running the App

Run the following command in your terminal:

```bash
streamlit run app.py
