import streamlit as st
import requests
import math
from datetime import date


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heatwave Prediction",
    page_icon="🌡️",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f7f9fc 0%, #eef2f7 100%);
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #1f2937;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Section headers */
    .section-title {
        font-size: 23px;
        font-weight: 700;
        color: #1f2937;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Result cards */
    .result-card {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    }

    .heatwave-card {
        background: #fff1f2;
        border: 2px solid #fb7185;
    }

    .safe-card {
        background: #f0fdf4;
        border: 2px solid #4ade80;
    }

    .result-title {
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .probability {
        font-size: 48px;
        font-weight: 800;
        margin: 10px;
    }

    .info-box {
        background: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 55px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌡️ Heatwave Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered heatwave risk prediction using Machine Learning + MLOps'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ System Information")

    st.write("### Architecture")

    st.write("""
    **Streamlit UI**
    
    ↓
    
    **Flask REST API**
    
    ↓
    
    **ML Model**
    """)

    st.divider()

    st.write("### 🤖 Model")

    st.write("HistGradientBoosting")

    st.write("300 estimators")

    st.divider()

    st.write("### 📊 Model Performance")

    st.metric("F1 Score", "0.7654")
    st.metric("Accuracy", "96.94%")
    st.metric("Recall", "95.59%")


# ============================================================
# LOCATION
# ============================================================

st.markdown(
    '<div class="section-title">📍 Location</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=19.0760,
        format="%.4f"
    )

with col2:
    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=72.8777,
        format="%.4f"
    )


# ============================================================
# DATE
# ============================================================

st.markdown(
    '<div class="section-title">📅 Date Information</div>',
    unsafe_allow_html=True
)

selected_date = st.date_input(
    "Select date",
    value=date(2025, 5, 20)
)

year = selected_date.year
month = selected_date.month
day_of_year = selected_date.timetuple().tm_yday


# ============================================================
# AUTOMATIC DATE FEATURES
# ============================================================

day_of_year_sin = math.sin(
    2 * math.pi * day_of_year / 365.0
)

day_of_year_cos = math.cos(
    2 * math.pi * day_of_year / 365.0
)

month_sin = math.sin(
    2 * math.pi * month / 12.0
)

month_cos = math.cos(
    2 * math.pi * month / 12.0
)

# Monsoon season: June to September
is_monsoon_season = 1 if month in [6, 7, 8, 9] else 0


# ============================================================
# TEMPERATURE
# ============================================================

st.markdown(
    '<div class="section-title">🌡️ Temperature</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    temp_min_c = st.number_input(
        "Minimum Temperature (°C)",
        value=28.0,
        step=0.1
    )

with col2:
    apparent_temp_min_c = st.number_input(
        "Apparent Minimum Temperature (°C)",
        value=30.0,
        step=0.1
    )


# ============================================================
# PRECIPITATION
# ============================================================

st.markdown(
    '<div class="section-title">🌧️ Precipitation</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    precipitation_mm = st.number_input(
        "Precipitation (mm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with col2:
    rain_mm = st.number_input(
        "Rain (mm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with col3:
    snowfall_cm = st.number_input(
        "Snowfall (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

precipitation_hours = st.number_input(
    "Precipitation Hours",
    min_value=0.0,
    max_value=24.0,
    value=0.0,
    step=0.1
)


# ============================================================
# WIND
# ============================================================

st.markdown(
    '<div class="section-title">💨 Wind Conditions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    wind_speed_max_kmh = st.number_input(
        "Maximum Wind Speed (km/h)",
        min_value=0.0,
        value=20.0,
        step=0.1
    )

with col2:
    wind_gusts_max_kmh = st.number_input(
        "Maximum Wind Gusts (km/h)",
        min_value=0.0,
        value=30.0,
        step=0.1
    )

with col3:
    wind_direction_dominant_deg = st.number_input(
        "Dominant Wind Direction (°)",
        min_value=0.0,
        max_value=360.0,
        value=270.0,
        step=1.0
    )


# ============================================================
# SUN / SOLAR CONDITIONS
# ============================================================

st.markdown(
    '<div class="section-title">☀️ Solar & Daylight Conditions</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    sunshine_duration_sec = st.number_input(
        "Sunshine Duration (seconds)",
        min_value=0.0,
        value=30000.0,
        step=100.0
    )

with col2:
    daylight_duration_sec = st.number_input(
        "Daylight Duration (seconds)",
        min_value=0.0,
        value=45000.0,
        step=100.0
    )

col1, col2 = st.columns(2)

with col1:
    solar_radiation_mj_m2 = st.number_input(
        "Solar Radiation (MJ/m²)",
        min_value=0.0,
        value=20.0,
        step=0.1
    )

with col2:
    reference_evapotranspiration_mm = st.number_input(
        "Reference Evapotranspiration (mm)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🔮 Generate Prediction</div>',
    unsafe_allow_html=True
)

predict_button = st.button(
    "🔥 PREDICT HEATWAVE",
    type="primary"
)


# ============================================================
# SEND DATA TO FLASK API
# ============================================================

if predict_button:

    # The payload must match the feature names expected
    # by the trained model.

    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "year": year,
        "month": month,
        "day_of_year": day_of_year,
        "temp_min_c": temp_min_c,
        "apparent_temp_min_c": apparent_temp_min_c,
        "precipitation_mm": precipitation_mm,
        "rain_mm": rain_mm,
        "snowfall_cm": snowfall_cm,
        "precipitation_hours": precipitation_hours,
        "is_monsoon_season": is_monsoon_season,
        "sunshine_duration_sec": sunshine_duration_sec,
        "daylight_duration_sec": daylight_duration_sec,
        "wind_speed_max_kmh": wind_speed_max_kmh,
        "wind_gusts_max_kmh": wind_gusts_max_kmh,
        "wind_direction_dominant_deg": wind_direction_dominant_deg,
        "solar_radiation_mj_m2": solar_radiation_mj_m2,
        "reference_evapotranspiration_mm": reference_evapotranspiration_mm,
        "day_of_year_sin": day_of_year_sin,
        "day_of_year_cos": day_of_year_cos,
        "month_sin": month_sin,
        "month_cos": month_cos
    }

    API_URL = "http://127.0.0.1:8000/predict"

    try:

        with st.spinner("Analyzing climate conditions..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

        if response.status_code == 200:

            result = response.json()

            prediction = result["heatwave_prediction"]
            probability = result["heatwave_probability"]

            probability_percent = probability * 100

            st.divider()

            # ==================================================
            # RESULT
            # ==================================================

            if prediction == 1:

                st.markdown(
                    f"""
                    <div class="result-card heatwave-card">
                        <div class="result-title">
                            🔴 HEATWAVE DETECTED
                        </div>
                        <div class="probability">
                            {probability_percent:.2f}%
                        </div>
                        <div>
                            Heatwave probability
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.error(
                    "⚠️ The model predicts conditions associated "
                    "with a heatwave."
                )

            else:

                st.markdown(
                    f"""
                    <div class="result-card safe-card">
                        <div class="result-title">
                            🟢 NO HEATWAVE
                        </div>
                        <div class="probability">
                            {probability_percent:.2f}%
                        </div>
                        <div>
                            Heatwave probability
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.success(
                    "✅ The model does not predict a heatwave "
                    "for these conditions."
                )

            # ==================================================
            # METRICS
            # ==================================================

            st.markdown("### 📊 Prediction Details")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Prediction",
                    "Heatwave" if prediction == 1
                    else "No Heatwave"
                )

            with col2:
                st.metric(
                    "Heatwave Probability",
                    f"{probability_percent:.2f}%"
                )

            with col3:
                st.metric(
                    "Monsoon Season",
                    "Yes" if is_monsoon_season else "No"
                )

            # Probability progress bar
            st.markdown("### 🌡️ Risk Probability")

            st.progress(
                min(max(probability, 0.0), 1.0)
            )

        else:

            st.error(
                f"Flask API returned an error "
                f"(HTTP {response.status_code})"
            )

            try:
                st.json(response.json())
            except Exception:
                st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to the Flask API."
        )

        st.info(
            "Make sure your Docker container is running "
            "on port 8000."
        )

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ The Flask API took too long to respond."
        )

    except Exception as e:

        st.error(
            f"Unexpected error: {str(e)}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#6b7280;">
        Heatwave Prediction System • Machine Learning + MLOps + DevOps
    </div>
    """,
    unsafe_allow_html=True
)