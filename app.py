import streamlit as st
import pandas as pd

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER v2.0
# Smart Money Detection & Institutional Intelligence Engine
# ============================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner v2.0",
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


/* TITLE */
.title {
    font-size: 40px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 5px;
}


/* SUBTITLE */
.subtitle {
    font-size: 18px;
    color: #A0A0A0;
    margin-bottom: 20px;
}


/* SECTION TITLE */
.section-title {
    color: #FFFFFF;
    font-size: 30px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
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


/* FORCE TEXT COLORS */
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
    font-weight: 800;
    margin-bottom: 18px;
}


/* PUT TITLE */
.put-title {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 18px;
}


/* GREEN */
.green-text {
    color: #00E676 !important;
    font-weight: 800;
}


/* RED */
.red-text {
    color: #FF1744 !important;
    font-weight: 800;
}


/* YELLOW */
.yellow-text {
    color: #FFD600 !important;
    font-weight: 800;
}


/* BLUE */
.blue-text {
    color: #42A5F5 !important;
    font-weight: 800;
}


/* DETAIL ROW */
.alert-detail {
    color: #FFFFFF !important;
    font-size: 18px;
    margin-bottom: 11px;
}


/* SCORE BOX */
.score-high {
    background-color: #0B5D32;
    color: #FFFFFF !important;
    padding: 10px 18px;
    border-radius: 8px;
    display: inline-block;
    font-size: 18px;
    font-weight: 800;
    margin-top: 10px;
}


.score-strong {
    background-color: #1565C0;
    color: #FFFFFF !important;
    padding: 10px 18px;
    border-radius: 8px;
    display: inline-block;
    font-size: 18px;
    font-weight: 800;
    margin-top: 10px;
}


.score-moderate {
    background-color: #8A6D00;
    color: #FFFFFF !important;
    padding: 10px 18px;
    border-radius: 8px;
    display: inline-block;
    font-size: 18px;
    font-weight: 800;
    margin-top: 10px;
}


.score-low {
    background-color: #555555;
    color: #FFFFFF !important;
    padding: 10px 18px;
    border-radius: 8px;
    display: inline-block;
    font-size: 18px;
    font-weight: 800;
    margin-top: 10px;
}


/* RANKING CARD */
.rank-card {
    background-color: #1A1F29;
    border: 1px solid #30363D;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    color: #FFFFFF !important;
}


/* METRIC LABEL */
[data-testid="stMetricLabel"] {
    color: #A0A0A0;
}


/* METRIC VALUE */
[data-testid="stMetricValue"] {
    color: #FFFFFF;
}


/* DIVIDER */
hr {
    border-color: #303030;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">📊 LK Institutional Options Flow Scanner v2.0</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Money Detection • Institutional Flow Intelligence Engine</div>',
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


minimum_score = st.sidebar.slider(
    "Minimum Institutional Score",
    min_value=0,
    max_value=100,
    value=0,
    step=5
)


st.sidebar.write("")


scan_button = st.sidebar.button(
    "🔍 Scan Institutional Flow",
    use_container_width=True
)


# ============================================================
# SAMPLE OPTIONS FLOW DATA
# ============================================================
#
# Future API structure:
# These fields can later be populated directly from
# an Options Flow provider.
#
# volume = contracts traded
# avg_volume = historical average option volume
# executions = number of separate executions
# execution_seconds = time window of executions
# premium = estimated trade premium
#
# ============================================================

sample_data = [

    {
        "ticker": "AAPL",
        "type": "CALL",
        "expiration": "Sep 10",
        "contracts": 2500,
        "strike": 325,
        "premium": 1800000,
        "avg_volume": 450,
        "executions": 8,
        "execution_seconds": 14,
        "aggression": "Aggressive Buy"
    },

    {
        "ticker": "NVDA",
        "type": "PUT",
        "expiration": "Sep 13",
        "contracts": 4200,
        "strike": 175,
        "premium": 3200000,
        "avg_volume": 600,
        "executions": 1,
        "execution_seconds": 2,
        "aggression": "Aggressive Buy"
    },

    {
        "ticker": "TSLA",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 1800,
        "strike": 350,
        "premium": 1450000,
        "avg_volume": 900,
        "executions": 3,
        "execution_seconds": 45,
        "aggression": "Aggressive Buy"
    },

    {
        "ticker": "QQQ",
        "type": "PUT",
        "expiration": "Sep 10",
        "contracts": 3100,
        "strike": 580,
        "premium": 2200000,
        "avg_volume": 500,
        "executions": 12,
        "execution_seconds": 20,
        "aggression": "Aggressive Sell"
    },

    {
        "ticker": "META",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 3600,
        "strike": 750,
        "premium": 3900000,
        "avg_volume": 400,
        "executions": 6,
        "execution_seconds": 10,
        "aggression": "Aggressive Buy"
    },

    {
        "ticker": "PLTR",
        "type": "CALL",
        "expiration": "Sep 20",
        "contracts": 1100,
        "strike": 200,
        "premium": 650000,
        "avg_volume": 800,
        "executions": 1,
        "execution_seconds": 5,
        "aggression": "Neutral"
    }

]


# ============================================================
# INTELLIGENCE ENGINE
# ============================================================

def analyze_flow(item):

    score = 0

    contracts = item["contracts"]
    avg_volume = item["avg_volume"]
    premium = item["premium"]
    executions = item["executions"]
    execution_seconds = item["execution_seconds"]


    # --------------------------------------------------------
    # VOLUME RATIO
    # --------------------------------------------------------

    if avg_volume > 0:
        volume_ratio = contracts / avg_volume
    else:
        volume_ratio = 1


    # --------------------------------------------------------
    # UNUSUAL VOLUME DETECTION
    # --------------------------------------------------------

    if volume_ratio >= 5:
        unusual_volume = "EXTREME"
        unusual_points = 30

    elif volume_ratio >= 3:
        unusual_volume = "HIGH"
        unusual_points = 22

    elif volume_ratio >= 2:
        unusual_volume = "MODERATE"
        unusual_points = 14

    else:
        unusual_volume = "NORMAL"
        unusual_points = 5


    score += unusual_points


    # --------------------------------------------------------
    # PREMIUM SCORE
    # --------------------------------------------------------

    if premium >= 3000000:
        premium_points = 25

    elif premium >= 1500000:
        premium_points = 20

    elif premium >= 750000:
        premium_points = 14

    else:
        premium_points = 7


    score += premium_points


    # --------------------------------------------------------
    # SWEEP DETECTION
    #
    # Multiple executions completed rapidly
    # --------------------------------------------------------

    is_sweep = False

    if executions >= 3 and execution_seconds <= 30:
        is_sweep = True
        score += 20


    # --------------------------------------------------------
    # BLOCK DETECTION
    #
    # Large transaction in few executions
    # --------------------------------------------------------

    is_block = False

    if contracts >= 2000 and executions <= 2:
        is_block = True
        score += 18


    # --------------------------------------------------------
    # AGGRESSIVE TRANSACTION SCORE
    # --------------------------------------------------------

    if item["aggression"] == "Aggressive Buy":
        score += 15

    elif item["aggression"] == "Aggressive Sell":
        score += 10

    else:
        score += 4


    # --------------------------------------------------------
    # CONTRACT SIZE SCORE
    # --------------------------------------------------------

    if contracts >= 4000:
        score += 15

    elif contracts >= 2500:
        score += 10

    elif contracts >= 1000:
        score += 5


    # --------------------------------------------------------
    # LIMIT SCORE TO 100
    # --------------------------------------------------------

    score = min(score, 100)


    # --------------------------------------------------------
    # FLOW ACTIVITY LABEL
    # --------------------------------------------------------

    if is_sweep and is_block:
        activity = "SWEEP + BLOCK"

    elif is_sweep:
        activity = "SWEEP"

    elif is_block:
        activity = "BLOCK TRADE"

    else:
        activity = "STANDARD FLOW"


    # --------------------------------------------------------
    # INSTITUTIONAL CONFIDENCE
    # --------------------------------------------------------

    if score >= 90:
        confidence = "EXTREME INSTITUTIONAL FLOW"

    elif score >= 75:
        confidence = "STRONG INSTITUTIONAL FLOW"

    elif score >= 60:
        confidence = "MODERATE INSTITUTIONAL FLOW"

    elif score >= 40:
        confidence = "NEUTRAL FLOW"

    else:
        confidence = "LOW CONVICTION"


    return {
        "score": score,
        "volume_ratio": round(volume_ratio, 1),
        "unusual_volume": unusual_volume,
        "is_sweep": is_sweep,
        "is_block": is_block,
        "activity": activity,
        "confidence": confidence
    }


# ============================================================
# ANALYZE ALL FLOWS
# ============================================================

processed_data = []


for item in sample_data:

    analysis = analyze_flow(item)

    new_item = item.copy()

    new_item.update(analysis)

    processed_data.append(new_item)


# ============================================================
# FILTER DATA
# ============================================================

filtered_data = []


for item in processed_data:

    if item["ticker"] not in selected_tickers:
        continue

    if item["contracts"] < minimum_contracts:
        continue

    if item["premium"] < minimum_premium:
        continue

    if item["score"] < minimum_score:
        continue

    if flow_type == "CALLS" and item["type"] != "CALL":
        continue

    if flow_type == "PUTS" and item["type"] != "PUT":
        continue

    filtered_data.append(item)


# ============================================================
# SORT BY INSTITUTIONAL SCORE
# ============================================================

filtered_data = sorted(
    filtered_data,
    key=lambda x: x["score"],
    reverse=True
)


# ============================================================
# METRICS
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


col1, col2, col3, col4, col5 = st.columns(5)


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
        "⚡ SWEEPS",
        len([
            x for x in filtered_data
            if x["is_sweep"]
        ])
    )


with col4:
    st.metric(
        "💰 CALL PREMIUM",
        f"${call_premium:,.0f}"
    )


with col5:
    st.metric(
        "💰 PUT PREMIUM",
        f"${put_premium:,.0f}"
    )


st.write("")
st.divider()


# ============================================================
# TOP INSTITUTIONAL FLOWS
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Top Institutional Flow Ranking</div>',
    unsafe_allow_html=True
)


if len(filtered_data) > 0:

    ranking_data = []

    for item in filtered_data[:5]:

        direction = "🟢 CALL" if item["type"] == "CALL" else "🔴 PUT"

        ranking_data.append({
            "Ticker": item["ticker"],
            "Direction": direction,
            "Activity": item["activity"],
            "Premium": f"${item['premium']:,.0f}",
            "Volume Ratio": f"{item['volume_ratio']}x",
            "Score": f"{item['score']}/100"
        })


    ranking_df = pd.DataFrame(ranking_data)

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )


else:

    st.info("No institutional flows meet the current filter criteria.")


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
# SCORE CLASS
# ============================================================

def get_score_class(score):

    if score >= 90:
        return "score-high"

    elif score >= 75:
        return "score-strong"

    elif score >= 60:
        return "score-moderate"

    else:
        return "score-low"


# ============================================================
# DISPLAY ALERTS
# ============================================================

if len(filtered_data) == 0:

    st.warning(
        "No institutional options flow detected based on current filters."
    )


else:

    for item in filtered_data:


        score_class = get_score_class(
            item["score"]
        )


        # ====================================================
        # BULLISH CALL
        # ====================================================

        if item["type"] == "CALL":

            sweep_text = "⚡ YES" if item["is_sweep"] else "NO"
            block_text = "🧱 YES" if item["is_block"] else "NO"


            call_html = f"""<div class="call-box">

<div class="call-title">
🟢 {item["ticker"]} —
<span class="green-text">CALL</span>
BUYING DETECTED
</div>

<div class="alert-detail">
<b>Institutional Activity:</b>
<span class="green-text">{item["activity"]}</span>
</div>

<div class="alert-detail">
<b>Institutional Score:</b>
<span class="green-text">{item["score"]}/100</span>
</div>

<div class="alert-detail">
<b>Confidence:</b>
<span class="green-text">{item["confidence"]}</span>
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
<b>Volume vs Average:</b>
<span class="yellow-text">{item["volume_ratio"]}x</span>
</div>

<div class="alert-detail">
<b>Unusual Volume:</b>
<span class="yellow-text">{item["unusual_volume"]}</span>
</div>

<div class="alert-detail">
<b>Sweep Detected:</b> {sweep_text}
</div>

<div class="alert-detail">
<b>Block Trade:</b> {block_text}
</div>

<div class="alert-detail">
<b>Transaction:</b>
<span class="green-text">{item["aggression"]}</span>
</div>

<div class="alert-detail">
<b>Signal:</b>
<span class="green-text">
🟢 Bullish Institutional Flow
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

            sweep_text = "⚡ YES" if item["is_sweep"] else "NO"
            block_text = "🧱 YES" if item["is_block"] else "NO"


            put_html = f"""<div class="put-box">

<div class="put-title">
🔴 {item["ticker"]} —
<span class="red-text">PUT</span>
BUYING DETECTED
</div>

<div class="alert-detail">
<b>Institutional Activity:</b>
<span class="red-text">{item["activity"]}</span>
</div>

<div class="alert-detail">
<b>Institutional Score:</b>
<span class="red-text">{item["score"]}/100</span>
</div>

<div class="alert-detail">
<b>Confidence:</b>
<span class="red-text">{item["confidence"]}</span>
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
<b>Volume vs Average:</b>
<span class="yellow-text">{item["volume_ratio"]}x</span>
</div>

<div class="alert-detail">
<b>Unusual Volume:</b>
<span class="yellow-text">{item["unusual_volume"]}</span>
</div>

<div class="alert-detail">
<b>Sweep Detected:</b> {sweep_text}
</div>

<div class="alert-detail">
<b>Block Trade:</b> {block_text}
</div>

<div class="alert-detail">
<b>Transaction:</b>
<span class="red-text">{item["aggression"]}</span>
</div>

<div class="alert-detail">
<b>Signal:</b>
<span class="red-text">
🔴 Bearish Institutional Flow
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
    "LK Institutional Options Flow Scanner v2.0 • "
    "Institutional Intelligence Engine • Smart Money Detection"
)
