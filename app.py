import streamlit as st
import pandas as pd
import html

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #151d2b;
    color: #e8edf5;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #253142;
    border-right: 1px solid #39475b;
}

[data-testid="stSidebar"] * {
    color: #e8edf5;
}


/* Main Title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #f1f3f7;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #aeb7c5;
    margin-bottom: 35px;
}


/* Metric Cards */
.metric-card {
    background: #222d3d;
    border: 1px solid #35445a;
    border-radius: 16px;
    padding: 22px;
    min-height: 115px;
}

.metric-label {
    color: #aeb7c5;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.metric-value {
    color: #f3f5f8;
    font-size: 32px;
    font-weight: 800;
    margin-top: 8px;
}


/* Section Titles */
.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #f1f3f7;
    margin-top: 30px;
    margin-bottom: 20px;
}


/* Divider */
.custom-divider {
    border-top: 1px solid #344052;
    margin-top: 45px;
    margin-bottom: 40px;
}


/* Institutional Flow Cards */
.flow-card {
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
    width: 100%;
    box-sizing: border-box;
}

.call-card {
    background: linear-gradient(135deg, #173d30, #1b342b);
    border-left: 6px solid #58d69b;
}

.put-card {
    background: linear-gradient(135deg, #4b282d, #44262b);
    border-left: 6px solid #ff5964;
}


/* Flow Header */
.flow-card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 25px;
}

.flow-title {
    font-size: 24px;
    font-weight: 800;
    color: #f4f5f7;
}

.call-highlight {
    color: #62d69d;
}

.put-highlight {
    color: #ff737d;
}


/* Confidence */
.confidence-call {
    background-color: rgba(88, 214, 155, 0.15);
    color: #62d69d;
    border: 1px solid rgba(88, 214, 155, 0.35);
    padding: 8px 14px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 13px;
    white-space: nowrap;
}

.confidence-put {
    background-color: rgba(255, 89, 100, 0.15);
    color: #ff737d;
    border: 1px solid rgba(255, 89, 100, 0.35);
    padding: 8px 14px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 13px;
    white-space: nowrap;
}


/* Score */
.score-call {
    font-size: 17px;
    font-weight: 800;
    color: #62d69d;
}

.score-put {
    font-size: 17px;
    font-weight: 800;
    color: #ff737d;
}


/* Info Grid */
.info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
}

.info-box {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 12px;
    padding: 14px;
}

.info-label {
    font-size: 12px;
    color: #aeb7c5;
    margin-bottom: 7px;
}

.info-value {
    font-size: 16px;
    font-weight: 700;
    color: #f2f4f7;
}

.call-value {
    color: #62d69d;
}

.put-value {
    color: #ff737d;
}

.gold-value {
    color: #f2c96d;
}


/* Signal Footer */
.signal-box {
    margin-top: 22px;
    padding-top: 18px;
    border-top: 1px solid rgba(255, 255, 255, 0.10);
    font-size: 17px;
    font-weight: 700;
    color: #f2f4f7;
}


/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* Sidebar Button */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    background-color: #2c3a4e;
    color: white;
    border: 1px solid #465873;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: #34465d;
    border-color: #62d69d;
}


/* Responsive */
@media (max-width: 900px) {

    .info-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .flow-card-header {
        flex-direction: column;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SAMPLE INSTITUTIONAL FLOW DATA
# =========================================================

flow_data = [

    {
        "ticker": "META",
        "direction": "CALL",
        "activity": "SWEEP",
        "premium": 3900000,
        "volume_ratio": 9.0,
        "score": 95,
        "expiration": "Sep 13",
        "contracts": 3600,
        "strike": 750,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Buy",
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "NVDA",
        "direction": "PUT",
        "activity": "BLOCK TRADE",
        "premium": 3200000,
        "volume_ratio": 7.0,
        "score": 95,
        "expiration": "Sep 13",
        "contracts": 4200,
        "strike": 175,
        "unusual_volume": "EXTREME",
        "sweep": "NO",
        "block_trade": "YES",
        "transaction": "Aggressive Sell",
        "signal": "Bearish Institutional Flow"
    },

    {
        "ticker": "QQQ",
        "direction": "PUT",
        "activity": "SWEEP",
        "premium": 2200000,
        "volume_ratio": 6.2,
        "score": 85,
        "expiration": "Sep 10",
        "contracts": 3100,
        "strike": 580,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Sell",
        "signal": "Bearish Institutional Flow"
    },

    {
        "ticker": "SPY",
        "direction": "CALL",
        "activity": "SWEEP",
        "premium": 2100000,
        "volume_ratio": 4.9,
        "score": 80,
        "expiration": "Sep 10",
        "contracts": 2800,
        "strike": 650,
        "unusual_volume": "HIGH",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Buy",
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "AAPL",
        "direction": "CALL",
        "activity": "SWEEP",
        "premium": 1800000,
        "volume_ratio": 5.6,
        "score": 75,
        "expiration": "Sep 10",
        "contracts": 2500,
        "strike": 325,
        "unusual_volume": "EXTREME",
        "sweep": "YES",
        "block_trade": "NO",
        "transaction": "Aggressive Buy",
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "NFLX",
        "direction": "CALL",
        "activity": "BLOCK TRADE",
        "premium": 1200000,
        "volume_ratio": 3.8,
        "score": 60,
        "expiration": "Sep 20",
        "contracts": 1500,
        "strike": 1250,
        "unusual_volume": "HIGH",
        "sweep": "NO",
        "block_trade": "YES",
        "transaction": "Aggressive Buy",
        "signal": "Bullish Institutional Flow"
    },

    {
        "ticker": "MSFT",
        "direction": "PUT",
        "activity": "STANDARD FLOW",
        "premium": 750000,
        "volume_ratio": 2.4,
        "score": 45,
        "expiration": "Sep 20",
        "contracts": 1200,
        "strike": 480,
        "unusual_volume": "MODERATE",
        "sweep": "NO",
        "block_trade": "NO",
        "transaction": "Neutral",
        "signal": "Moderate Bearish Flow"
    },

    {
        "ticker": "TSLA",
        "direction": "CALL",
        "activity": "STANDARD FLOW",
        "premium": 1450000,
        "volume_ratio": 2.0,
        "score": 40,
        "expiration": "Sep 13",
        "contracts": 1800,
        "strike": 350,
        "unusual_volume": "MODERATE",
        "sweep": "NO",
        "block_trade": "NO",
        "transaction": "Aggressive Buy",
        "signal": "Low Bullish Conviction"
    },

    {
        "ticker": "PLTR",
        "direction": "CALL",
        "activity": "STANDARD FLOW",
        "premium": 650000,
        "volume_ratio": 1.4,
        "score": 20,
        "expiration": "Sep 20",
        "contracts": 1100,
        "strike": 200,
        "unusual_volume": "NORMAL",
        "sweep": "NO",
        "block_trade": "NO",
        "transaction": "Neutral",
        "signal": "Low Bullish Conviction"
    }
]

df = pd.DataFrame(flow_data)


# =========================================================
# SIDEBAR CONTROLS
# =========================================================

st.sidebar.markdown("## ⚙️ Scanner Controls")

all_tickers = sorted(df["ticker"].unique().tolist())

selected_tickers = st.sidebar.multiselect(
    "Select Tickers",
    options=all_tickers,
    default=all_tickers
)

min_contracts = st.sidebar.slider(
    "Minimum Contracts",
    min_value=0,
    max_value=5000,
    value=1000,
    step=100
)

min_premium = st.sidebar.slider(
    "Minimum Premium ($)",
    min_value=0,
    max_value=5000000,
    value=100000,
    step=50000
)

flow_type = st.sidebar.radio(
    "Flow Type",
    ["All", "CALLS", "PUTS"]
)

st.sidebar.markdown("---")

scan_button = st.sidebar.button("🔍 Scan Institutional Flow")


# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = df.copy()

# If no ticker is selected, show no results
if len(selected_tickers) == 0:
    filtered_df = filtered_df.iloc[0:0]
else:
    filtered_df = filtered_df[
        filtered_df["ticker"].isin(selected_tickers)
    ]

filtered_df = filtered_df[
    filtered_df["contracts"] >= min_contracts
]

filtered_df = filtered_df[
    filtered_df["premium"] >= min_premium
]

if flow_type == "CALLS":
    filtered_df = filtered_df[
        filtered_df["direction"] == "CALL"
    ]

elif flow_type == "PUTS":
    filtered_df = filtered_df[
        filtered_df["direction"] == "PUT"
    ]


filtered_df = filtered_df.sort_values(
    by=["score", "premium"],
    ascending=[False, False]
).reset_index(drop=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
    📊 LK Institutional Options Flow Scanner
</div>

<div class="subtitle">
    Smart Money Detection • Institutional Options Activity • High Conviction Flow Analysis
</div>
""", unsafe_allow_html=True)


# =========================================================
# EMPTY RESULT
# =========================================================

if filtered_df.empty:

    st.warning(
        "No institutional options flow matches your current scanner filters."
    )

    st.stop()


# =========================================================
# METRICS
# =========================================================

bullish_count = len(
    filtered_df[
        filtered_df["direction"] == "CALL"
    ]
)

bearish_count = len(
    filtered_df[
        filtered_df["direction"] == "PUT"
    ]
)

call_premium = filtered_df.loc[
    filtered_df["direction"] == "CALL",
    "premium"
].sum()

put_premium = filtered_df.loc[
    filtered_df["direction"] == "PUT",
    "premium"
].sum()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🟢 BULLISH CALL FLOW</div>
        <div class="metric-value">{bullish_count}</div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🔴 BEARISH PUT FLOW</div>
        <div class="metric-value">{bearish_count}</div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">💰 CALL PREMIUM</div>
        <div class="metric-value">${call_premium:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">💰 PUT PREMIUM</div>
        <div class="metric-value">${put_premium:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# DIVIDER
# =========================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)


# =========================================================
# TOP INSTITUTIONAL FLOW RANKING
# =========================================================

st.markdown(
    '<div class="section-title">🏆 Top Institutional Flow Ranking</div>',
    unsafe_allow_html=True
)


display_df = filtered_df[
    [
        "ticker",
        "direction",
        "activity",
        "premium",
        "volume_ratio",
        "score"
    ]
].copy()


display_df.columns = [
    "Ticker",
    "Direction",
    "Activity",
    "Premium",
    "Volume Ratio",
    "Score"
]


display_df["Direction"] = display_df["Direction"].apply(
    lambda x: "🟢 CALL" if x == "CALL" else "🔴 PUT"
)

display_df["Premium"] = display_df["Premium"].apply(
    lambda x: f"${x:,.0f}"
)

display_df["Volume Ratio"] = display_df["Volume Ratio"].apply(
    lambda x: f"{x:.1f}x"
)

display_df["Score"] = display_df["Score"].apply(
    lambda x: f"{x}/100"
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# DIVIDER
# =========================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)


# =========================================================
# HIGHEST CONVICTION TRADE
# =========================================================

st.markdown(
    '<div class="section-title">🔥 Highest Conviction Institutional Trade</div>',
    unsafe_allow_html=True
)


highest_trade = filtered_df.iloc[0]


# =========================================================
# CONFIDENCE FUNCTION
# =========================================================

def get_confidence(score):

    if score >= 90:
        return "EXTREME INSTITUTIONAL FLOW"

    elif score >= 75:
        return "HIGH CONVICTION"

    elif score >= 50:
        return "MODERATE CONVICTION"

    elif score >= 30:
        return "NEUTRAL FLOW"

    else:
        return "LOW CONVICTION"


# =========================================================
# FLOW CARD FUNCTION
# =========================================================

def create_flow_card(trade):

    ticker = html.escape(str(trade["ticker"]))
    direction = html.escape(str(trade["direction"]))
    activity = html.escape(str(trade["activity"]))
    expiration = html.escape(str(trade["expiration"]))
    unusual_volume = html.escape(str(trade["unusual_volume"]))
    transaction = html.escape(str(trade["transaction"]))
    signal = html.escape(str(trade["signal"]))

    score = int(trade["score"])
    contracts = int(trade["contracts"])
    strike = float(trade["strike"])
    premium = float(trade["premium"])
    volume_ratio = float(trade["volume_ratio"])

    confidence = get_confidence(score)

    if direction == "CALL":

        card_class = "flow-card call-card"
        confidence_class = "confidence-call"
        score_class = "score-call"
        value_class = "call-value"

        direction_html = '<span class="call-highlight">CALL</span>'
        signal_icon = "🟢"

    else:

        card_class = "flow-card put-card"
        confidence_class = "confidence-put"
        score_class = "score-put"
        value_class = "put-value"

        direction_html = '<span class="put-highlight">PUT</span>'
        signal_icon = "🔴"

    sweep_icon = "⚡" if trade["sweep"] == "YES" else ""
    block_icon = "🧱" if trade["block_trade"] == "YES" else ""

    card_html = f"""
<div class="{card_class}">

    <div class="flow-card-header">

        <div class="flow-title">
            {signal_icon} {ticker} — {direction_html}
            <br>
            <span style="font-size:15px; color:#aeb7c5;">
                BUYING DETECTED
            </span>
        </div>

        <div>
            <span class="{confidence_class}">
                {confidence}
            </span>
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
            <div class="info-label">Institutional Score</div>
            <div class="info-value {score_class}">
                {score}/100
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Expiration</div>
            <div class="info-value">
                {expiration}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Contracts</div>
            <div class="info-value">
                {contracts:,} {direction}S
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Strike</div>
            <div class="info-value">
                ${strike:,.0f}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Premium</div>
            <div class="info-value gold-value">
                ${premium:,.0f}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Volume vs Average</div>
            <div class="info-value gold-value">
                {volume_ratio:.1f}x
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Unusual Volume</div>
            <div class="info-value gold-value">
                {unusual_volume}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Sweep Detected</div>
            <div class="info-value">
                {sweep_icon} {trade["sweep"]}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Block Trade</div>
            <div class="info-value">
                {block_icon} {trade["block_trade"]}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Transaction</div>
            <div class="info-value {value_class}">
                {transaction}
            </div>
        </div>


        <div class="info-box">
            <div class="info-label">Signal</div>
            <div class="info-value {value_class}">
                {signal_icon} {signal}
            </div>
        </div>

    </div>


    <div class="signal-box">
        Institutional Smart Money Signal:
        <span class="{value_class}">
            {signal}
        </span>
    </div>

</div>
"""

    return card_html


# =========================================================
# DISPLAY HIGHEST CONVICTION CARD
# =========================================================

st.markdown(
    create_flow_card(highest_trade),
    unsafe_allow_html=True
)


# =========================================================
# DIVIDER
# =========================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)


# =========================================================
# INSTITUTIONAL OPTIONS FLOW ALERTS
# =========================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


remaining_trades = filtered_df.iloc[1:].reset_index(drop=True)


for index in range(0, len(remaining_trades), 2):

    col_left, col_right = st.columns(2)

    with col_left:

        trade = remaining_trades.iloc[index]

        st.markdown(
            create_flow_card(trade),
            unsafe_allow_html=True
        )

    if index + 1 < len(remaining_trades):

        with col_right:

            trade = remaining_trades.iloc[index + 1]

            st.markdown(
                create_flow_card(trade),
                unsafe_allow_html=True
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="
    text-align:center;
    color:#718096;
    padding:30px;
    font-size:14px;
">
    LK Institutional Options Flow Scanner
    • Smart Money Detection Engine
</div>
""", unsafe_allow_html=True)
