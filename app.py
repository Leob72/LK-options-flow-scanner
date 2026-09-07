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
# CUSTOM CSS - DARK INSTITUTIONAL DASHBOARD
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


/* CARD TITLES */

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


/* BUTTONS */

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

st.markdown(
    '<div class="main-title">📊 LK Institutional Options Flow Scanner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Money Detection • Institutional Options Activity • High Conviction Flow Analysis</div>',
    unsafe_allow_html=True
)


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

st.sidebar.divider()

scan_button = st.sidebar.button(
    "🔍 Scan Institutional Flow",
    use_container_width=True
)


# ============================================================
# SAMPLE DATA
# FUTURE: CONNECT TO REAL OPTIONS FLOW API
# ============================================================

sample_data = [

    {
        "ticker": "META",
        "type": "CALL",
        "activity": "SWEEP",
        "expiration": "Sep 13",
        "contracts": 3600,
        "strike": 750,
        "premium": 3900000,
        "volume_ratio": 9.0,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "NVDA",
        "type": "PUT",
        "activity": "BLOCK TRADE",
        "expiration": "Sep 13",
        "contracts": 4200,
        "strike": 175,
        "premium": 3200000,
        "volume_ratio": 7.0,
        "unusual_volume": "EXTREME",
        "sweep": "NO",
        "block_trade": "YES",
        "transaction": "Aggressive Sell"
    },

    {
        "ticker": "QQQ",
        "type": "PUT",
        "activity": "SWEEP",
        "expiration": "Sep 10",
        "contracts": 3100,
        "strike": 580,
        "premium": 2200000,
        "volume_ratio": 6.2,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Sell"
    },

    {
        "ticker": "AAPL",
        "type": "CALL",
        "activity": "SWEEP",
        "expiration": "Sep 10",
        "contracts": 2500,
        "strike": 325,
        "premium": 1800000,
        "volume_ratio": 5.6,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "TSLA",
        "type": "CALL",
        "activity": "STANDARD FLOW",
        "expiration": "Sep 13",
        "contracts": 1800,
        "strike": 350,
        "premium": 1450000,
        "volume_ratio": 2.0,
        "unusual_volume": "MODERATE",
        "sweep": "NO",
        "block_trade": "NO",
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "PLTR",
        "type": "CALL",
        "activity": "STANDARD FLOW",
        "expiration": "Sep 20",
        "contracts": 1100,
        "strike": 200,
        "premium": 650000,
        "volume_ratio": 1.4,
        "unusual_volume": "NORMAL",
        "sweep": "NO",
        "block_trade": "NO",
        "transaction": "Neutral"
    }

]


# ============================================================
# INSTITUTIONAL SCORE CALCULATION
# ============================================================

def calculate_score(item):

    score = 0

    # Volume Ratio
    ratio = item["volume_ratio"]

    if ratio >= 8:
        score += 35
    elif ratio >= 6:
        score += 30
    elif ratio >= 4:
        score += 25
    elif ratio >= 2:
        score += 15
    else:
        score += 5

    # Premium Size
    premium = item["premium"]

    if premium >= 3000000:
        score += 30
    elif premium >= 2000000:
        score += 25
    elif premium >= 1000000:
        score += 20
    elif premium >= 500000:
        score += 10

    # Sweep
    if item["sweep"] == "YES":
        score += 20

    # Block Trade
    if item["block_trade"] == "YES":
        score += 20

    # Contract Size
    contracts = item["contracts"]

    if contracts >= 4000:
        score += 15
    elif contracts >= 2500:
        score += 10
    elif contracts >= 1000:
        score += 5

    return min(score, 100)


# ============================================================
# CONFIDENCE CALCULATION
# ============================================================

def calculate_confidence(score):

    if score >= 90:
        return "EXTREME INSTITUTIONAL FLOW"
    elif score >= 75:
        return "HIGH CONVICTION"
    elif score >= 55:
        return "MODERATE CONVICTION"
    elif score >= 35:
        return "NEUTRAL FLOW"
    else:
        return "LOW CONVICTION"


# ============================================================
# SIGNAL CALCULATION
# ============================================================

def calculate_signal(item):

    score = item["score"]

    if item["type"] == "CALL":

        if score >= 75:
            return "Bullish Institutional Flow"
        elif score >= 50:
            return "Moderate Bullish Flow"
        else:
            return "Low Bullish Conviction"

    else:

        if score >= 75:
            return "Bearish Institutional Flow"
        elif score >= 50:
            return "Moderate Bearish Flow"
        else:
            return "Low Bearish Conviction"


# ============================================================
# ADD SCORES TO DATA
# ============================================================

for item in sample_data:

    item["score"] = calculate_score(item)
    item["confidence"] = calculate_confidence(item["score"])
    item["signal"] = calculate_signal(item)


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
# SUMMARY METRICS
# ============================================================

bullish_flows = len([
    x for x in filtered_data
    if x["type"] == "CALL"
])

bearish_flows = len([
    x for x in filtered_data
    if x["type"] == "PUT"
])

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


# ============================================================
# METRICS DISPLAY
# ============================================================

st.write("")

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


st.divider()


# ============================================================
# TOP INSTITUTIONAL FLOW RANKING
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Top Institutional Flow Ranking</div>',
    unsafe_allow_html=True
)

if len(filtered_data) > 0:

    ranking_data = []

    sorted_flows = sorted(
        filtered_data,
        key=lambda x: x["score"],
        reverse=True
    )

    for item in sorted_flows:

        direction = (
            "🟢 CALL"
            if item["type"] == "CALL"
            else "🔴 PUT"
        )

        ranking_data.append({
            "Ticker": item["ticker"],
            "Direction": direction,
            "Activity": item["activity"],
            "Premium": f"${item['premium']:,.0f}",
            "Volume Ratio": f"{item['volume_ratio']:.1f}x",
            "Score": f"{item['score']}/100"
        })

    ranking_df = pd.DataFrame(ranking_data)

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No institutional options flow detected with the current filters."
    )


st.divider()


# ============================================================
# FUNCTION TO BUILD ALERT CARD
# ============================================================

def render_alert_card(item):

    is_call = item["type"] == "CALL"

    card_class = "call-card" if is_call else "put-card"
    direction_class = "bullish" if is_call else "bearish"
    type_class = "call-text" if is_call else "put-text"

    icon = "🟢" if is_call else "🔴"
    option_name = "CALL" if is_call else "PUT"
    contracts_name = "CALLS" if is_call else "PUTS"

    sweep_text = "⚡ YES" if item["sweep"] == "YES" else "NO"
    block_text = "🧱 YES" if item["block_trade"] == "YES" else "NO"

    html = f"""
<div class="alert-card {card_class}">

<div class="card-title">
{icon} {item["ticker"]} —
<span class="{type_class}">{option_name}</span>
BUYING DETECTED
</div>

<div class="card-line">
<span class="label">Institutional Activity:</span>
<span class="{direction_class}">{item["activity"]}</span>
</div>

<div class="card-line">
<span class="label">Institutional Score:</span>
<span class="{direction_class}">{item["score"]}/100</span>
</div>

<div class="card-line">
<span class="label">Confidence:</span>
<span class="{direction_class}">{item["confidence"]}</span>
</div>

<div class="card-line">
<span class="label">Expiration:</span>
{item["expiration"]}
</div>

<div class="card-line">
<span class="label">Contracts:</span>
{item["contracts"]:,}
<span class="{direction_class}">{contracts_name}</span>
</div>

<div class="card-line">
<span class="label">Strike:</span>
${item["strike"]}
</div>

<div class="card-line">
<span class="label">Premium:</span>
${item["premium"]:,.0f}
</div>

<div class="card-line">
<span class="label">Volume vs Average:</span>
<span class="warning-text">{item["volume_ratio"]:.1f}x</span>
</div>

<div class="card-line">
<span class="label">Unusual Volume:</span>
<span class="warning-text">{item["unusual_volume"]}</span>
</div>

<div class="card-line">
<span class="label">Sweep Detected:</span>
{sweep_text}
</div>

<div class="card-line">
<span class="label">Block Trade:</span>
{block_text}
</div>

<div class="card-line">
<span class="label">Transaction:</span>
<span class="{direction_class}">{item["transaction"]}</span>
</div>

<div class="card-line">
<span class="label">Signal:</span>
<span class="{direction_class}">{icon} {item["signal"]}</span>
</div>

</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# HIGHEST CONVICTION INSTITUTIONAL TRADE
# ============================================================

if len(filtered_data) > 0:

    top_trade = max(
        filtered_data,
        key=lambda x: x["score"]
    )

    st.markdown(
        '<div class="section-title">🔥 Highest Conviction Institutional Trade</div>',
        unsafe_allow_html=True
    )

    render_alert_card(top_trade)


st.divider()


# ============================================================
# INSTITUTIONAL OPTIONS FLOW ALERTS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


# ============================================================
# DISPLAY ALL ALERTS
# ============================================================

if len(filtered_data) == 0:

    st.warning(
        "No institutional options flow detected based on current filters."
    )

else:

    sorted_alerts = sorted(
        filtered_data,
        key=lambda x: x["score"],
        reverse=True
    )

    for item in sorted_alerts:
        render_alert_card(item)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "LK Institutional Options Flow Scanner v2.0 • "
    "Smart Money Detection Dashboard • "
    "Institutional Flow Analysis"
)
