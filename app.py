import streamlit as st
import pandas as pd


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
   METRICS
   ============================================================ */

[data-testid="stMetric"] {
    background-color: #191F2B;
    border: 1px solid #2A3342;
    padding: 18px;
    border-radius: 12px;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #171C26;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: #2A3342 !important;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* ============================================================
   COMPACT ALERT CARDS
   ============================================================ */

.flow-card {
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid #2A3342;
    min-height: 370px;
}

.call-flow-card {
    background: linear-gradient(
        135deg,
        #173D2D,
        #123125
    );
    border-left: 5px solid #20E68A;
}

.put-flow-card {
    background: linear-gradient(
        135deg,
        #4A252B,
        #351B20
    );
    border-left: 5px solid #FF3B57;
}


/* ============================================================
   CARD HEADER
   ============================================================ */

.flow-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 15px;
    border-bottom: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 18px;
}

.flow-title {
    font-size: 25px;
    font-weight: 800;
    color: #F1F1F1;
}

.call-highlight {
    color: #32E89A;
}

.put-highlight {
    color: #FF6075;
}


/* ============================================================
   SCORE BADGE
   ============================================================ */

.score-call {
    background-color: rgba(32,230,138,0.15);
    color: #32E89A;
    border: 1px solid #32E89A;
    padding: 7px 12px;
    border-radius: 10px;
    font-weight: 800;
    font-size: 16px;
}

.score-put {
    background-color: rgba(255,59,87,0.15);
    color: #FF6075;
    border: 1px solid #FF6075;
    padding: 7px 12px;
    border-radius: 10px;
    font-weight: 800;
    font-size: 16px;
}


/* ============================================================
   CONFIDENCE
   ============================================================ */

.confidence-call {
    color: #32E89A;
    font-weight: 800;
    font-size: 15px;
}

.confidence-put {
    color: #FF6075;
    font-weight: 800;
    font-size: 15px;
}


/* ============================================================
   CARD GRID
   ============================================================ */

.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.info-box {
    background-color: rgba(0,0,0,0.16);
    padding: 11px;
    border-radius: 10px;
}

.info-label {
    font-size: 12px;
    color: #A9AFB8;
    margin-bottom: 4px;
}

.info-value {
    font-size: 16px;
    font-weight: 700;
    color: #EDEDED;
}


/* ============================================================
   SPECIAL VALUES
   ============================================================ */

.premium-value {
    color: #FFD166;
    font-weight: 800;
}

.call-value {
    color: #32E89A;
    font-weight: 800;
}

.put-value {
    color: #FF6075;
    font-weight: 800;
}


/* ============================================================
   CARD FOOTER
   ============================================================ */

.card-footer {
    margin-top: 18px;
    padding-top: 14px;
    border-top: 1px solid rgba(255,255,255,0.12);
}

.signal-call {
    color: #32E89A;
    font-weight: 800;
    font-size: 16px;
}

.signal-put {
    color: #FF6075;
    font-weight: 800;
    font-size: 16px;
}


/* ============================================================
   HIGHEST CONVICTION CARD
   ============================================================ */

.top-conviction-card {
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer-text {
    color: #7F8794;
    text-align: center;
    padding: 20px;
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

    # VOLUME RATIO
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


    # PREMIUM SIZE
    premium = item["premium"]

    if premium >= 3000000:
        score += 30

    elif premium >= 2000000:
        score += 25

    elif premium >= 1000000:
        score += 20

    elif premium >= 500000:
        score += 10


    # SWEEP
    if item["sweep"] == "YES":
        score += 20


    # BLOCK TRADE
    if item["block_trade"] == "YES":
        score += 20


    # CONTRACT SIZE
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
# FUNCTION TO CREATE COMPACT FLOW CARD
# ============================================================

def create_flow_card(item, top_card=False):

    ticker = item["ticker"]
    option_type = item["type"]
    score = item["score"]
    confidence = item["confidence"]
    activity = item["activity"]
    expiration = item["expiration"]
    contracts = item["contracts"]
    strike = item["strike"]
    premium = item["premium"]
    volume_ratio = item["volume_ratio"]
    unusual_volume = item["unusual_volume"]
    sweep = item["sweep"]
    block_trade = item["block_trade"]
    transaction = item["transaction"]
    signal = item["signal"]


    # ========================================================
    # CALL CARD
    # ========================================================

    if option_type == "CALL":

        card_class = "call-flow-card"
        score_class = "score-call"
        confidence_class = "confidence-call"
        value_class = "call-value"
        signal_class = "signal-call"

        icon = "🟢"

        html = f"""
<div class="flow-card {card_class}">

    <div class="flow-card-header">

        <div>
            <div class="flow-title">
                {icon} {ticker} —
                <span class="call-highlight">CALL</span>
            </div>

            <div class="{confidence_class}">
                {confidence}
            </div>
        </div>

        <div class="{score_class}">
            {score}/100
        </div>

    </div>


    <div class="info-grid">

        <div class="info-box">
            <div class="info-label">Institutional Activity</div>
            <div class="info-value {value_class}">
                {activity}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Premium</div>
            <div class="info-value premium-value">
                ${premium:,.0f}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Expiration</div>
            <div class="info-value">
                {expiration}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Strike</div>
            <div class="info-value">
                ${strike}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Contracts</div>
            <div class="info-value {value_class}">
                {contracts:,} CALLS
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Volume vs Average</div>
            <div class="info-value premium-value">
                {volume_ratio:.1f}x
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Unusual Volume</div>
            <div class="info-value premium-value">
                {unusual_volume}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Transaction</div>
            <div class="info-value {value_class}">
                {transaction}
            </div>
        </div>

    </div>


    <div class="card-footer">

        <div class="info-grid">

            <div>
                <div class="info-label">Sweep</div>
                <div class="info-value">
                    {"⚡ YES" if sweep == "YES" else "NO"}
                </div>
            </div>

            <div>
                <div class="info-label">Block Trade</div>
                <div class="info-value">
                    {"🧱 YES" if block_trade == "YES" else "NO"}
                </div>
            </div>

        </div>

        <br>

        <div class="{signal_class}">
            🟢 {signal}
        </div>

    </div>

</div>
"""

    # ========================================================
    # PUT CARD
    # ========================================================

    else:

        card_class = "put-flow-card"
        score_class = "score-put"
        confidence_class = "confidence-put"
        value_class = "put-value"
        signal_class = "signal-put"

        icon = "🔴"

        html = f"""
<div class="flow-card {card_class}">

    <div class="flow-card-header">

        <div>
            <div class="flow-title">
                {icon} {ticker} —
                <span class="put-highlight">PUT</span>
            </div>

            <div class="{confidence_class}">
                {confidence}
            </div>
        </div>

        <div class="{score_class}">
            {score}/100
        </div>

    </div>


    <div class="info-grid">

        <div class="info-box">
            <div class="info-label">Institutional Activity</div>
            <div class="info-value {value_class}">
                {activity}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Premium</div>
            <div class="info-value premium-value">
                ${premium:,.0f}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Expiration</div>
            <div class="info-value">
                {expiration}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Strike</div>
            <div class="info-value">
                ${strike}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Contracts</div>
            <div class="info-value {value_class}">
                {contracts:,} PUTS
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Volume vs Average</div>
            <div class="info-value premium-value">
                {volume_ratio:.1f}x
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Unusual Volume</div>
            <div class="info-value premium-value">
                {unusual_volume}
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Transaction</div>
            <div class="info-value {value_class}">
                {transaction}
            </div>
        </div>

    </div>


    <div class="card-footer">

        <div class="info-grid">

            <div>
                <div class="info-label">Sweep</div>
                <div class="info-value">
                    {"⚡ YES" if sweep == "YES" else "NO"}
                </div>
            </div>

            <div>
                <div class="info-label">Block Trade</div>
                <div class="info-value">
                    {"🧱 YES" if block_trade == "YES" else "NO"}
                </div>
            </div>

        </div>

        <br>

        <div class="{signal_class}">
            🔴 {signal}
        </div>

    </div>

</div>
"""

    return html


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

    st.markdown(
        create_flow_card(top_trade, top_card=True),
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
# DISPLAY ALL ALERTS IN 2 COLUMNS
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

    # Create rows with 2 cards each
    for i in range(0, len(sorted_alerts), 2):

        col1, col2 = st.columns(2)

        # LEFT CARD
        with col1:

            if i < len(sorted_alerts):

                st.markdown(
                    create_flow_card(sorted_alerts[i]),
                    unsafe_allow_html=True
                )


        # RIGHT CARD
        with col2:

            if i + 1 < len(sorted_alerts):

                st.markdown(
                    create_flow_card(sorted_alerts[i + 1]),
                    unsafe_allow_html=True
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '''
    <div class="footer-text">
        LK Institutional Options Flow Scanner v2.1
        <br>
        Smart Money Detection Dashboard • Institutional Flow Analysis
    </div>
    ''',
    unsafe_allow_html=True
)
