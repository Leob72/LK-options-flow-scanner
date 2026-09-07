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

/* ============================================================
   MAIN APP
   ============================================================ */

.stApp {
    background-color: #11151F;
    color: #E8E8E8;
}

.main {
    background-color: #11151F;
}


/* ============================================================
   HEADER
   ============================================================ */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #F1F1F1;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #A9AFB8;
    margin-bottom: 25px;
}


/* ============================================================
   ALERT CARDS
   ============================================================ */

.alert-card {
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 22px;
    color: #EAEAEA;
}

.call-card {
    background-color: #163D2C;
    border-left: 7px solid #20E68A;
}

.put-card {
    background-color: #482126;
    border-left: 7px solid #FF3B57;
}


/* ============================================================
   CARD TITLE
   ============================================================ */

.card-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 25px;
    color: #F2F2F2;
}

.call-text {
    color: #32E89A !important;
}

.put-text {
    color: #FF4560 !important;
}


/* ============================================================
   CARD TEXT
   ============================================================ */

.card-line {
    font-size: 19px;
    font-weight: 500;
    margin: 13px 0;
    color: #D8D8D8;
}

.label {
    font-weight: 750;
    color: #E5E5E5;
}

.bullish {
    color: #32E89A !important;
    font-weight: 800;
}

.bearish {
    color: #FF4560 !important;
    font-weight: 800;
}

.warning-text {
    color: #FFD54A !important;
    font-weight: 800;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #F0F0F0;
    margin-top: 20px;
    margin-bottom: 20px;
}


/* ============================================================
   HIGHEST CONVICTION CARD
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
}


/* ============================================================
   METRICS
   ============================================================ */

[data-testid="stMetric"] {
    background-color: #191F2B;
    border: 1px solid #2A3342;
    padding: 18px;
    border-radius: 12px;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: #2A3342 !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #171C26;
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

    # --------------------------------------------------------
    # VOLUME RATIO
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # PREMIUM SIZE
    # --------------------------------------------------------

    premium = item["premium"]

    if premium >= 3000000:
        score += 30

    elif premium >= 2000000:
        score += 25

    elif premium >= 1000000:
        score += 20

    elif premium >= 500000:
        score += 10


    # --------------------------------------------------------
    # SWEEP
    # --------------------------------------------------------

    if item["sweep"] == "YES":
        score += 20


    # --------------------------------------------------------
    # BLOCK TRADE
    # --------------------------------------------------------

    if item["block_trade"] == "YES":
        score += 20


    # --------------------------------------------------------
    # CONTRACT SIZE
    # --------------------------------------------------------

    contracts = item["contracts"]

    if contracts >= 4000:
        score += 15

    elif contracts >= 2500:
        score += 10

    elif contracts >= 1000:
        score += 5


    # Maximum Score = 100

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

    item["confidence"] = calculate_confidence(
        item["score"]
    )

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


    # --------------------------------------------------------
    # CALL HIGHEST CONVICTION
    # --------------------------------------------------------

    if top_trade["type"] == "CALL":

        conviction_html = f"""
<div class="alert-card call-card">

<div class="card-title">
🟢 {top_trade["ticker"]} —
<span class="call-text">CALL</span>
BUYING DETECTED
</div>

<div class="card-line">
<span class="label">Institutional Activity:</span>
<span class="bullish">{top_trade["activity"]}</span>
</div>

<div class="card-line">
<span class="label">Institutional Score:</span>
<span class="bullish">{top_trade["score"]}/100</span>
</div>

<div class="card-line">
<span class="label">Confidence:</span>
<span class="bullish">{top_trade["confidence"]}</span>
</div>

<div class="card-line">
<span class="label">Expiration:</span>
{top_trade["expiration"]}
</div>

<div class="card-line">
<span class="label">Contracts:</span>
{top_trade["contracts"]:,}
<span class="bullish">CALLS</span>
</div>

<div class="card-line">
<span class="label">Strike:</span>
${top_trade["strike"]}
</div>

<div class="card-line">
<span class="label">Premium:</span>
${top_trade["premium"]:,.0f}
</div>

<div class="card-line">
<span class="label">Volume vs Average:</span>
<span class="warning-text">{top_trade["volume_ratio"]:.1f}x</span>
</div>

<div class="card-line">
<span class="label">Unusual Volume:</span>
<span class="warning-text">{top_trade["unusual_volume"]}</span>
</div>

<div class="card-line">
<span class="label">Sweep Detected:</span>
{"⚡ YES" if top_trade["sweep"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Block Trade:</span>
{"🧱 YES" if top_trade["block_trade"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Transaction:</span>
<span class="bullish">{top_trade["transaction"]}</span>
</div>

<div class="card-line">
<span class="label">Signal:</span>
<span class="bullish">🟢 {top_trade["signal"]}</span>
</div>

</div>
"""

    # --------------------------------------------------------
    # PUT HIGHEST CONVICTION
    # --------------------------------------------------------

    else:

        conviction_html = f"""
<div class="alert-card put-card">

<div class="card-title">
🔴 {top_trade["ticker"]} —
<span class="put-text">PUT</span>
BUYING DETECTED
</div>

<div class="card-line">
<span class="label">Institutional Activity:</span>
<span class="bearish">{top_trade["activity"]}</span>
</div>

<div class="card-line">
<span class="label">Institutional Score:</span>
<span class="bearish">{top_trade["score"]}/100</span>
</div>

<div class="card-line">
<span class="label">Confidence:</span>
<span class="bearish">{top_trade["confidence"]}</span>
</div>

<div class="card-line">
<span class="label">Expiration:</span>
{top_trade["expiration"]}
</div>

<div class="card-line">
<span class="label">Contracts:</span>
{top_trade["contracts"]:,}
<span class="bearish">PUTS</span>
</div>

<div class="card-line">
<span class="label">Strike:</span>
${top_trade["strike"]}
</div>

<div class="card-line">
<span class="label">Premium:</span>
${top_trade["premium"]:,.0f}
</div>

<div class="card-line">
<span class="label">Volume vs Average:</span>
<span class="warning-text">{top_trade["volume_ratio"]:.1f}x</span>
</div>

<div class="card-line">
<span class="label">Unusual Volume:</span>
<span class="warning-text">{top_trade["unusual_volume"]}</span>
</div>

<div class="card-line">
<span class="label">Sweep Detected:</span>
{"⚡ YES" if top_trade["sweep"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Block Trade:</span>
{"🧱 YES" if top_trade["block_trade"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Transaction:</span>
<span class="bearish">{top_trade["transaction"]}</span>
</div>

<div class="card-line">
<span class="label">Signal:</span>
<span class="bearish">🔴 {top_trade["signal"]}</span>
</div>

</div>
"""


    # IMPORTANT:
    # Render HTML explicitly
    st.markdown(
        conviction_html,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# INSTITUTIONAL OPTIONS FLOW ALERTS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


# ============================================================
# FUNCTION TO RENDER ALERT CARD
# ============================================================

def render_alert_card(item):

    if item["type"] == "CALL":

        html = f"""
<div class="alert-card call-card">

<div class="card-title">
🟢 {item["ticker"]} —
<span class="call-text">CALL</span>
BUYING DETECTED
</div>

<div class="card-line">
<span class="label">Institutional Activity:</span>
<span class="bullish">{item["activity"]}</span>
</div>

<div class="card-line">
<span class="label">Institutional Score:</span>
<span class="bullish">{item["score"]}/100</span>
</div>

<div class="card-line">
<span class="label">Confidence:</span>
<span class="bullish">{item["confidence"]}</span>
</div>

<div class="card-line">
<span class="label">Expiration:</span>
{item["expiration"]}
</div>

<div class="card-line">
<span class="label">Contracts:</span>
{item["contracts"]:,}
<span class="bullish">CALLS</span>
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
{"⚡ YES" if item["sweep"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Block Trade:</span>
{"🧱 YES" if item["block_trade"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Transaction:</span>
<span class="bullish">{item["transaction"]}</span>
</div>

<div class="card-line">
<span class="label">Signal:</span>
<span class="bullish">🟢 {item["signal"]}</span>
</div>

</div>
"""

    else:

        html = f"""
<div class="alert-card put-card">

<div class="card-title">
🔴 {item["ticker"]} —
<span class="put-text">PUT</span>
BUYING DETECTED
</div>

<div class="card-line">
<span class="label">Institutional Activity:</span>
<span class="bearish">{item["activity"]}</span>
</div>

<div class="card-line">
<span class="label">Institutional Score:</span>
<span class="bearish">{item["score"]}/100</span>
</div>

<div class="card-line">
<span class="label">Confidence:</span>
<span class="bearish">{item["confidence"]}</span>
</div>

<div class="card-line">
<span class="label">Expiration:</span>
{item["expiration"]}
</div>

<div class="card-line">
<span class="label">Contracts:</span>
{item["contracts"]:,}
<span class="bearish">PUTS</span>
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
{"⚡ YES" if item["sweep"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Block Trade:</span>
{"🧱 YES" if item["block_trade"] == "YES" else "NO"}
</div>

<div class="card-line">
<span class="label">Transaction:</span>
<span class="bearish">{item["transaction"]}</span>
</div>

<div class="card-line">
<span class="label">Signal:</span>
<span class="bearish">🔴 {item["signal"]}</span>
</div>

</div>
"""

    # This is the critical line that renders HTML
    st.markdown(
        html,
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
