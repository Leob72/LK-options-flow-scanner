import streamlit as st
import pandas as pd

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER v2.0
# Smart Money Detection Dashboard
# ============================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background-color: #151B26;
    color: #F1F5F9;
}

.main {
    background-color: #151B26;
}


/* HEADER */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #F8FAFC;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #AAB4C3;
    margin-bottom: 25px;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #1C2431;
    border-right: 1px solid #334155;
}

section[data-testid="stSidebar"] * {
    color: #E2E8F0;
}


/* METRIC CARDS */

[data-testid="stMetric"] {
    background-color: #202938;
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #AAB4C3 !important;
    font-size: 14px;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #F8FAFC !important;
    font-size: 30px;
    font-weight: 800;
}


/* ALERT CARDS */

.alert-card {
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 22px;
    color: #F1F5F9;
    border: 1px solid #334155;
}

.call-card {
    background-color: #173D2D;
    border-left: 7px solid #39D98A;
}

.put-card {
    background-color: #48232B;
    border-left: 7px solid #FF5C70;
}


/* CARD TITLE */

.card-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 25px;
    color: #F8FAFC;
}

.call-text {
    color: #39D98A !important;
}

.put-text {
    color: #FF5C70 !important;
}


/* CARD TEXT */

.card-line {
    font-size: 19px;
    font-weight: 500;
    margin: 13px 0;
    color: #E2E8F0;
}

.label {
    font-weight: 750;
    color: #F8FAFC;
}

.bullish {
    color: #39D98A !important;
    font-weight: 800;
}

.bearish {
    color: #FF5C70 !important;
    font-weight: 800;
}

.warning-text {
    color: #F4C95D !important;
    font-weight: 800;
}


/* SECTION TITLES */

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #F8FAFC;
    margin-top: 20px;
    margin-bottom: 20px;
}


/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #334155;
}


/* DIVIDERS */

hr {
    border-color: #334155 !important;
}


/* BUTTON */

.stButton > button {
    background-color: #263244;
    color: #F8FAFC;
    border: 1px solid #46556B;
    border-radius: 10px;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #39D98A;
    color: #39D98A;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================
/* ============================================================
   HEADER
   ============================================================ */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #F8FAFC;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #AAB4C3;
    margin-bottom: 25px;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #1C2431;
    border-right: 1px solid #334155;
}

section[data-testid="stSidebar"] * {
    color: #E2E8F0;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

[data-testid="stMetric"] {
    background-color: #202938;
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 14px;
}


/* Metric Label */

[data-testid="stMetricLabel"] {
    color: #AAB4C3 !important;
    font-size: 14px;
    font-weight: 600;
}


/* Metric Value */

[data-testid="stMetricValue"] {
    color: #F8FAFC !important;
    font-size: 30px;
    font-weight: 800;
}


/* ============================================================
   ALERT CARDS
   ============================================================ */

.alert-card {
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 22px;
    color: #F1F5F9;
    border: 1px solid #334155;
}


/* CALL CARD */

.call-card {
    background-color: #173D2D;
    border-left: 7px solid #39D98A;
}


/* PUT CARD */

.put-card {
    background-color: #48232B;
    border-left: 7px solid #FF5C70;
}


/* ============================================================
   CARD TITLE
   ============================================================ */

.card-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 25px;
    color: #F8FAFC;
}

.call-text {
    color: #39D98A !important;
}

.put-text {
    color: #FF5C70 !important;
}


/* ============================================================
   CARD TEXT
   ============================================================ */

.card-line {
    font-size: 19px;
    font-weight: 500;
    margin: 13px 0;
    color: #E2E8F0;
}

.label {
    font-weight: 750;
    color: #F8FAFC;
}


/* SIGNAL COLORS */

.bullish {
    color: #39D98A !important;
    font-weight: 800;
}

.bearish {
    color: #FF5C70 !important;
    font-weight: 800;
}

.warning-text {
    color: #F4C95D !important;
    font-weight: 800;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #F8FAFC;
    margin-top: 20px;
    margin-bottom: 20px;
}


/* ============================================================
   HIGHEST CONVICTION
   ============================================================ */

.conviction-container {
    padding: 8px;
    border-radius: 18px;
    margin-bottom: 30px;
}

.conviction-title {
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 20px;
    color: #F8FAFC;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #334155;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: #334155 !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {
    background-color: #263244;
    color: #F8FAFC;
    border: 1px solid #46556B;
    border-radius: 10px;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #39D98A;
    color: #39D98A;
}

</style>
""", unsafe_allow_html=True)
