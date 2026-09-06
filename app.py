import streamlit as st
import pandas as pd

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER
# Smart Money Detection Dashboard
# ============================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM STYLE
# ============================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background-color: #0E1117;
}


/* MAIN TITLE */
.title {
    font-size: 38px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 5px;
}


/* SUBTITLE */
.subtitle {
    font-size: 18px;
    color: #A0A0A0;
    margin-bottom: 25px;
}


/* CALL ALERT BOX */
.call-box {
    background-color: #123D2A;
    border-left: 7px solid #00E676;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 18px;
    color: #FFFFFF !important;
}


/* PUT ALERT BOX */
.put-box {
    background-color: #421C24;
    border-left: 7px solid #FF1744;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 18px;
    color: #FFFFFF !important;
}


/* FORCE WHITE TEXT INSIDE ALERT BOXES */
.call-box,
.call-box p,
.call-box b,
.call-box div {
    color: #FFFFFF !important;
}


.put-box,
.put-box p,
.put-box b,
.put-box div {
    color: #FFFFFF !important;
}


/* CALL TITLE */
.call-title {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 18px;
}


/* PUT TITLE */
.put-title {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 18px;
}


/* GREEN TEXT */
.green-text {
    color: #00E676 !important;
    font-weight: 700;
}


/* RED TEXT */
.red-text {
    color: #FF1744 !important;
    font-weight: 700;
}


/* DETAIL ROWS */
.alert-detail {
    color: #FFFFFF !important;
    font-size: 18px;
    margin-bottom: 10px;
}


/* SECTION TITLE */
.section-title {
    color: #FFFFFF;
    font-size: 30px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
}


/* DIVIDER */
hr {
    border-color: #303030;
}


/* METRIC LABEL */
[data-testid="stMetricLabel"] {
    color: #A0A0A0;
}


/* METRIC VALUE */
[data-testid="stMetricValue"] {
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">📊 LK Institutional Options Flow Scanner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Money Detection • Institutional Options Activity</div>',
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# SIDEBAR CONTROLS
# ============================================================

st.sidebar.markdown("## ⚙️ Scanner Controls")


tickers = [
    "AAPL",
    "NVDA",
    "TSLA",
    "PLTR",
    "QQQ",
    "SPY",
    "META",
    "AMZN",
    "NFLX",
    "MSFT"
]


selected_tickers = st.sidebar.multiselect(
    "Select Tickers",
    tickers,
    default=tickers
)


minimum_contracts = st.sidebar.slider(
    "Minimum Contracts",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)


minimum_premium = st.sidebar.slider(
    "Minimum Premium ($)",
    min_value=10000,
    max_value=5000000,
    value=100000,
    step=50000
)


flow_type = st.sidebar.radio(
    "Flow Type",
    ["All", "CALLS", "PUTS"]
)


st.sidebar.write("")


scan_button = st.sidebar.button(
    "🔍 Scan Institutional Flow",
    use_container_width=True
)


# ============================================================
# SAMPLE DATA
# ============================================================

sample_data = [

    {
        "ticker": "AAPL",
        "type": "CALL",
        "expiration": "Sep 10",
        "contracts": 2500,
        "strike": 325,
        "premium": 1800000,
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "NVDA",
        "type": "PUT",
        "expiration": "Sep 13",
        "contracts": 4200,
        "strike": 175,
        "premium": 3200000,
        "signal": "Bearish Institutional Flow"
    },

    {
        "ticker": "TSLA",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 1800,
        "strike": 350,
        "premium": 1450000,
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "QQQ",
        "type": "PUT",
        "expiration": "Sep 10",
        "contracts": 3100,
        "strike": 580,
        "premium": 2200000,
        "signal": "Bearish Institutional Flow"
    },

    {
        "ticker": "META",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 3600,
        "strike": 750,
        "premium": 3900000,
        "signal": "Bullish Institutional Flow"
    }

]


# ============================================================
# FILTER DATA
# ============================================================

filtered_data = []


for item in sample_data:

    if item["ticker"] not in selected_tickers:
        continue

    if item["contracts"] < minimum_contracts:
        continue

    if item["premium"] < minimum_premium:
        continue

    if flow_type == "CALLS" and item["type"] != "CALL":
        continue

    if flow_type == "PUTS" and item["type"] != "PUT":
        continue

    filtered_data.append(item)


# ============================================================
# METRICS
# ============================================================

bullish_flows = len(
    [
        x for x in filtered_data
        if x["type"] == "CALL"
    ]
)


bearish_flows = len(
    [
        x for x in filtered_data
        if x["type"] == "PUT"
    ]
)


call_premium = sum(
    x["premium"]
    for x in filtered_data
    if x["type"] == "CALL"
)


put_premium = sum(
    x["premium"]
    for x in filtered_data
    if x["type"] == "PUT"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🟢 BULLISH CALL FLOW",
        bullish_flows
    )


with col2:

    st.metric(
        "🔴 BEARISH PUT FLOW",
        bearish_flows
    )


with col3:

    st.metric(
        "💰 CALL PREMIUM",
        f"${call_premium:,.0f}"
    )


with col4:

    st.metric(
        "💰 PUT PREMIUM",
        f"${put_premium:,.0f}"
    )


st.write("")
st.divider()


# ============================================================
# ALERT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


# ============================================================
# DISPLAY ALERTS
# ============================================================

if len(filtered_data) == 0:

    st.warning(
        "No institutional options flow detected based on current filters."
    )


else:

    for item in filtered_data:


        # ====================================================
        # BULLISH CALL
        # ====================================================

        if item["type"] == "CALL":

            call_html = f"""<div class="call-box">
<div class="call-title">
🟢 {item["ticker"]} —
<span class="green-text">CALL</span>
BUYING DETECTED
</div>

<div class="alert-detail">
<b>Expiration:</b> {item["expiration"]}
</div>

<div class="alert-detail">
<b>Contracts:</b> {item["contracts"]:,}
<span class="green-text">CALLS</span>
</div>

<div class="alert-detail">
<b>Strike:</b> ${item["strike"]}
</div>

<div class="alert-detail">
<b>Premium:</b> ${item["premium"]:,.0f}
</div>

<div class="alert-detail">
<b>Type:</b> Aggressive Buy
</div>

<div class="alert-detail">
<b>Signal:</b>
<span class="green-text">
🟢 {item["signal"]}
</span>
</div>

</div>"""

            st.markdown(
                call_html,
                unsafe_allow_html=True
            )


        # ====================================================
        # BEARISH PUT
        # ====================================================

        elif item["type"] == "PUT":

            put_html = f"""<div class="put-box">
<div class="put-title">
🔴 {item["ticker"]} —
<span class="red-text">PUT</span>
BUYING DETECTED
</div>

<div class="alert-detail">
<b>Expiration:</b> {item["expiration"]}
</div>

<div class="alert-detail">
<b>Contracts:</b> {item["contracts"]:,}
<span class="red-text">PUTS</span>
</div>

<div class="alert-detail">
<b>Strike:</b> ${item["strike"]}
</div>

<div class="alert-detail">
<b>Premium:</b> ${item["premium"]:,.0f}
</div>

<div class="alert-detail">
<b>Type:</b> Aggressive Buy
</div>

<div class="alert-detail">
<b>Signal:</b>
<span class="red-text">
🔴 {item["signal"]}
</span>
</div>

</div>"""

            st.markdown(
                put_html,
                unsafe_allow_html=True
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    "LK Institutional Options Flow Scanner • "
    "Smart Money Detection Dashboard"
)
