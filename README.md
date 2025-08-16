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

## 🚀 Installation & Running the App (Windows)

Follow these steps to set up and run the Live Air Quality Tracker locally.

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/PranavKekunnaya/Live-Air-Quality-Tracker---West-Lafayette.git
cd Live-Air-Quality-Tracker---West-Lafayette

---

### 2️⃣ Create a virtual environment

python -m venv venv

### 3️⃣ Activate the virtual environment

PowerShell: .\venv\Scripts\Activate.ps1
If blocked by PowerShell, run once: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Command Prompt: .\venv\Scripts\activate.bat

### 4️⃣ Install dependencies:

pip install streamlit requests pandas plotly python-dotenv

### 5️⃣ Create a .env file

In the project root, create a file named .env with your OpenWeatherMap API key:

API_KEY=your_openweathermap_api_key_here

### 6️⃣ Run the app
streamlit run app.py

And your all set now!

