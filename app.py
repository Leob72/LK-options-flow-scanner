import streamlit as st
import pandas as pd
import textwrap

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER v2.1
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
    background-color: #111722;
    color: #E8EDF5;
}

.main {
    background-color: #111722;
}


/* ============================================================
   HEADER
   ============================================================ */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #F1F3F6;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #A9B2C1;
    margin-bottom: 25px;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #202A38;
}

section[data-testid="stSidebar"] * {
    color: #E8EDF5;
}


/* ============================================================
   METRICS
   ============================================================ */

[data-testid="stMetric"] {
    background-color: #1D2635;
    border: 1px solid #324155;
    padding: 18px;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #AAB4C2 !important;
}

[data-testid="stMetricValue"] {
    color: #F1F3F6 !important;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #F0F3F7;
    margin-top: 25px;
    margin-bottom: 20px;
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
    border-color: #303B4B !important;
}


/* ============================================================
   FLOW CARDS
   ============================================================ */

.flow-card {
    padding: 28px;
    border-radius: 16px;
    margin-bottom: 20px;
    min-height: 430px;
}

.call-card {
    background-color: #173B2D;
    border-left: 6px solid #45D995;
}

.put-card {
    background-color: #4A272C;
    border-left: 6px solid #FF5268;
}


/* ============================================================
   FLOW CARD HEADER
   ============================================================ */

.flow-card-header {
    margin-bottom: 25px;
}

.flow-title {
    font-size: 29px;
    font-weight: 800;
    color: #F1F3F6;
}

.call-highlight {
    color: #55E3A0;
}

.put-highlight {
    color: #FF6477;
}


/* ============================================================
   CONFIDENCE
   ============================================================ */

.confidence-call {
    display: inline-block;
    margin-top: 8px;
    padding: 6px 12px;
    border-radius: 20px;
    background-color: rgba(69, 217, 149, 0.15);
    color: #62E6AA;
    font-size: 14px;
    font-weight: 700;
}

.confidence-put {
    display: inline-block;
    margin-top: 8px;
    padding: 6px 12px;
    border-radius: 20px;
    background-color: rgba(255, 82, 104, 0.15);
    color: #FF7181;
    font-size: 14px;
    font-weight: 700;
}


/* ============================================================
   SCORE
   ============================================================ */

.score-call {
    margin-top: 12px;
    font-size: 20px;
    font-weight: 800;
    color: #55E3A0;
}

.score-put {
    margin-top: 12px;
    font-size: 20px;
    font-weight: 800;
    color: #FF6477;
}


/* ============================================================
   INFO GRID
   ============================================================ */

.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 22px;
}

.info-box {
    background-color: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 14px;
}

.info-label {
    font-size: 13px;
    color: #AAB4C2;
    margin-bottom: 6px;
}

.info-value {
    font-size: 16px;
    font-weight: 700;
    color: #F1F3F6;
}

.call-value {
    color: #55E3A0;
}

.put-value {
    color: #FF6477;
}

.warning-value {
    color: #FFD166;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 900px) {

    .info-grid {
        grid-template-columns: 1fr;
    }

    .flow-title {
        font-size: 24px;
    }

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


    premium = item["premium"]

    if premium >= 3000000:
        score += 30
    elif premium >= 2000000:
        score += 25
    elif premium >= 1000000:
        score += 20
    elif premium >= 500000:
        score += 10


    if item["sweep"] == "YES":
        score += 20


    if item["block_trade"] == "YES":
        score += 20


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
# ADD SCORES
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

bullish_flows = len(
    [x for x in filtered_data if x["type"] == "CALL"]
)


bearish_flows = len(
    [x for x in filtered_data if x["type"] == "PUT"]
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
# FUNCTION TO RENDER FLOW CARD
# IMPORTANT: textwrap.dedent prevents HTML from rendering as text
# ============================================================

def render_flow_card(item):

    is_call = item["type"] == "CALL"

    if is_call:

        card_class = "call-card"
        highlight_class = "call-highlight"
        confidence_class = "confidence-call"
        score_class = "score-call"
        value_class = "call-value"

        direction_icon = "🟢"
        direction_text = "CALL"

    else:

        card_class = "put-card"
        highlight_class = "put-highlight"
        confidence_class = "confidence-put"
        score_class = "score-put"
        value_class = "put-value"

        direction_icon = "🔴"
        direction_text = "PUT"


    sweep_display = (
        "⚡ YES"
        if item["sweep"] == "YES"
        else "NO"
    )


    block_display = (
        "🧱 YES"
        if item["block_trade"] == "YES"
        else "NO"
    )


    html = textwrap.dedent(f"""
    <div class="flow-card {card_class}">

        <div class="flow-card-header">

            <div class="flow-title">
                {direction_icon} {item["ticker"]} —
                <span class="{highlight_class}">
                    {direction_text}
                </span>
                BUYING DETECTED
            </div>

            <div class="{confidence_class}">
                {item["confidence"]}
            </div>

            <div class="{score_class}">
                Institutional Score: {item["score"]}/100
            </div>

        </div>


        <div class="info-grid">

            <div class="info-box">
                <div class="info-label">
                    Institutional Activity
                </div>
                <div class="info-value {value_class}">
                    {item["activity"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Premium
                </div>
                <div class="info-value">
                    ${item["premium"]:,.0f}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Expiration
                </div>
                <div class="info-value">
                    {item["expiration"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Contracts
                </div>
                <div class="info-value {value_class}">
                    {item["contracts"]:,} {direction_text}S
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Strike
                </div>
                <div class="info-value">
                    ${item["strike"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Volume vs Average
                </div>
                <div class="info-value warning-value">
                    {item["volume_ratio"]:.1f}x
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Unusual Volume
                </div>
                <div class="info-value warning-value">
                    {item["unusual_volume"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Sweep Detected
                </div>
                <div class="info-value">
                    {sweep_display}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Block Trade
                </div>
                <div class="info-value">
                    {block_display}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Transaction
                </div>
                <div class="info-value {value_class}">
                    {item["transaction"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Signal
                </div>
                <div class="info-value {value_class}">
                    {direction_icon} {item["signal"]}
                </div>
            </div>


            <div class="info-box">
                <div class="info-label">
                    Flow Type
                </div>
                <div class="info-value {value_class}">
                    {direction_text}
                </div>
            </div>

        </div>

    </div>
    """)

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# HIGHEST CONVICTION INSTITUTIONAL TRADE
# ============================================================

if len(filtered_data) > 0:

    st.markdown(
        '<div class="section-title">🔥 Highest Conviction Institutional Trade</div>',
        unsafe_allow_html=True
    )


    top_trade = max(
        filtered_data,
        key=lambda x: x["score"]
    )


    render_flow_card(top_trade)


st.divider()


# ============================================================
# INSTITUTIONAL OPTIONS FLOW ALERTS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


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


    # Display cards in two columns
    for i in range(0, len(sorted_alerts), 2):

        col1, col2 = st.columns(2)


        with col1:
            render_flow_card(sorted_alerts[i])


        if i + 1 < len(sorted_alerts):

            with col2:
                render_flow_card(sorted_alerts[i + 1])


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    "LK Institutional Options Flow Scanner v2.1 • "
    "Smart Money Detection Dashboard • "
    "Institutional Flow Analysis"
)
