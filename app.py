import streamlit as st
import pandas as pd
import html


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ----------------------------------------------------------
   MAIN APP
---------------------------------------------------------- */

.stApp {
    background-color: #111827;
    color: #E5E7EB;
}


/* ----------------------------------------------------------
   REMOVE EXTRA TOP SPACE
---------------------------------------------------------- */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ----------------------------------------------------------
   SIDEBAR
---------------------------------------------------------- */

[data-testid="stSidebar"] {
    background-color: #1F2937;
    border-right: 1px solid #374151;
}

[data-testid="stSidebar"] * {
    color: #E5E7EB;
}


/* ----------------------------------------------------------
   HEADER
---------------------------------------------------------- */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #F3F4F6;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #9CA3AF;
    margin-bottom: 30px;
}


/* ----------------------------------------------------------
   METRIC CARDS
---------------------------------------------------------- */

.metric-card {
    background-color: #1F2937;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 24px;
    min-height: 120px;
}

.metric-label {
    font-size: 14px;
    color: #9CA3AF;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #F3F4F6;
    margin-top: 8px;
}

.metric-green {
    color: #6EE7B7;
}

.metric-red {
    color: #FB7185;
}

.metric-gold {
    color: #FBBF24;
}


/* ----------------------------------------------------------
   SECTION TITLES
---------------------------------------------------------- */

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #F3F4F6;
    margin-top: 30px;
    margin-bottom: 20px;
}


/* ----------------------------------------------------------
   DIVIDER
---------------------------------------------------------- */

.divider {
    border-top: 1px solid #374151;
    margin-top: 25px;
    margin-bottom: 25px;
}


/* ----------------------------------------------------------
   TABLE
---------------------------------------------------------- */

.dataframe {
    font-size: 15px;
}


/* ----------------------------------------------------------
   FLOW CARD
---------------------------------------------------------- */

.flow-card {
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 20px;
    border-left: 6px solid #6EE7B7;
    background: linear-gradient(
        135deg,
        #163B2C,
        #18372B
    );
}

.flow-card-put {
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 20px;
    border-left: 6px solid #FB7185;
    background: linear-gradient(
        135deg,
        #48262C,
        #3A2026
    );
}


/* ----------------------------------------------------------
   FLOW CARD HEADER
---------------------------------------------------------- */

.flow-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 25px;
}

.flow-title {
    font-size: 28px;
    font-weight: 800;
    color: #F3F4F6;
}

.call-highlight {
    color: #6EE7B7;
}

.put-highlight {
    color: #FB7185;
}


/* ----------------------------------------------------------
   CONFIDENCE
---------------------------------------------------------- */

.confidence-call {
    background-color: rgba(34, 197, 94, 0.15);
    color: #6EE7B7;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
}

.confidence-put {
    background-color: rgba(239, 68, 68, 0.15);
    color: #FB7185;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
}


/* ----------------------------------------------------------
   SCORE
---------------------------------------------------------- */

.score-call {
    font-size: 22px;
    font-weight: 800;
    color: #6EE7B7;
}

.score-put {
    font-size: 22px;
    font-weight: 800;
    color: #FB7185;
}


/* ----------------------------------------------------------
   INFO GRID
---------------------------------------------------------- */

.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
}

.info-box {
    background-color: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 14px;
}

.info-label {
    font-size: 13px;
    color: #9CA3AF;
    margin-bottom: 5px;
}

.info-value {
    font-size: 17px;
    font-weight: 700;
    color: #F3F4F6;
}

.call-value {
    color: #6EE7B7;
}

.put-value {
    color: #FB7185;
}

.gold-value {
    color: #FBBF24;
}


/* ----------------------------------------------------------
   ALERT GRID
---------------------------------------------------------- */

.alert-grid-title {
    font-size: 30px;
    font-weight: 800;
    color: #F3F4F6;
    margin-top: 25px;
    margin-bottom: 20px;
}


/* ----------------------------------------------------------
   FOOTER
---------------------------------------------------------- */

.footer {
    color: #6B7280;
    font-size: 13px;
    text-align: center;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SAMPLE DATA
# ============================================================
# Later we can replace this section with real options flow data.

data = [
    {
        "Ticker": "META",
        "Direction": "CALL",
        "Activity": "SWEEP",
        "Premium": 3900000,
        "Volume Ratio": 9.0,
        "Score": 95,
        "Expiration": "Sep 13",
        "Contracts": 3600,
        "Strike": 750,
        "Unusual Volume": "EXTREME",
        "Sweep Detected": "YES",
        "Block Trade": "NO",
        "Transaction": "Aggressive Buy",
        "Signal": "Bullish Institutional Flow"
    },
    {
        "Ticker": "NVDA",
        "Direction": "PUT",
        "Activity": "BLOCK TRADE",
        "Premium": 3200000,
        "Volume Ratio": 7.0,
        "Score": 95,
        "Expiration": "Sep 13",
        "Contracts": 4200,
        "Strike": 175,
        "Unusual Volume": "EXTREME",
        "Sweep Detected": "NO",
        "Block Trade": "YES",
        "Transaction": "Aggressive Sell",
        "Signal": "Bearish Institutional Flow"
    },
    {
        "Ticker": "QQQ",
        "Direction": "PUT",
        "Activity": "SWEEP",
        "Premium": 2200000,
        "Volume Ratio": 6.2,
        "Score": 85,
        "Expiration": "Sep 10",
        "Contracts": 3100,
        "Strike": 580,
        "Unusual Volume": "EXTREME",
        "Sweep Detected": "YES",
        "Block Trade": "NO",
        "Transaction": "Aggressive Sell",
        "Signal": "Bearish Institutional Flow"
    },
    {
        "Ticker": "AAPL",
        "Direction": "CALL",
        "Activity": "SWEEP",
        "Premium": 1800000,
        "Volume Ratio": 5.6,
        "Score": 75,
        "Expiration": "Sep 10",
        "Contracts": 2500,
        "Strike": 325,
        "Unusual Volume": "EXTREME",
        "Sweep Detected": "YES",
        "Block Trade": "NO",
        "Transaction": "Aggressive Buy",
        "Signal": "Bullish Institutional Flow"
    },
    {
        "Ticker": "TSLA",
        "Direction": "CALL",
        "Activity": "STANDARD FLOW",
        "Premium": 1450000,
        "Volume Ratio": 2.0,
        "Score": 40,
        "Expiration": "Sep 13",
        "Contracts": 1800,
        "Strike": 350,
        "Unusual Volume": "MODERATE",
        "Sweep Detected": "NO",
        "Block Trade": "NO",
        "Transaction": "Aggressive Buy",
        "Signal": "Low Bullish Conviction"
    },
    {
        "Ticker": "PLTR",
        "Direction": "CALL",
        "Activity": "STANDARD FLOW",
        "Premium": 650000,
        "Volume Ratio": 1.4,
        "Score": 20,
        "Expiration": "Sep 20",
        "Contracts": 1100,
        "Strike": 200,
        "Unusual Volume": "NORMAL",
        "Sweep Detected": "NO",
        "Block Trade": "NO",
        "Transaction": "Neutral",
        "Signal": "Low Bullish Conviction"
    },
    {
        "Ticker": "AMZN",
        "Direction": "PUT",
        "Activity": "STANDARD FLOW",
        "Premium": 480000,
        "Volume Ratio": 1.3,
        "Score": 15,
        "Expiration": "Sep 20",
        "Contracts": 900,
        "Strike": 210,
        "Unusual Volume": "NORMAL",
        "Sweep Detected": "NO",
        "Block Trade": "NO",
        "Transaction": "Neutral",
        "Signal": "Low Bearish Conviction"
    },
    {
        "Ticker": "NFLX",
        "Direction": "CALL",
        "Activity": "BLOCK TRADE",
        "Premium": 1200000,
        "Volume Ratio": 3.8,
        "Score": 60,
        "Expiration": "Sep 13",
        "Contracts": 1400,
        "Strike": 1300,
        "Unusual Volume": "HIGH",
        "Sweep Detected": "NO",
        "Block Trade": "YES",
        "Transaction": "Aggressive Buy",
        "Signal": "Bullish Institutional Flow"
    },
    {
        "Ticker": "MSFT",
        "Direction": "PUT",
        "Activity": "STANDARD FLOW",
        "Premium": 750000,
        "Volume Ratio": 2.4,
        "Score": 45,
        "Expiration": "Sep 13",
        "Contracts": 1200,
        "Strike": 500,
        "Unusual Volume": "MODERATE",
        "Sweep Detected": "NO",
        "Block Trade": "NO",
        "Transaction": "Aggressive Sell",
        "Signal": "Moderate Bearish Flow"
    },
    {
        "Ticker": "SPY",
        "Direction": "CALL",
        "Activity": "SWEEP",
        "Premium": 2100000,
        "Volume Ratio": 4.9,
        "Score": 80,
        "Expiration": "Sep 10",
        "Contracts": 3500,
        "Strike": 650,
        "Unusual Volume": "EXTREME",
        "Sweep Detected": "YES",
        "Block Trade": "NO",
        "Transaction": "Aggressive Buy",
        "Signal": "High Conviction Bullish Flow"
    }
]


df = pd.DataFrame(data)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_currency(value):
    return "${:,.0f}".format(value)


def get_confidence(score):

    if score >= 90:
        return "EXTREME INSTITUTIONAL FLOW"

    elif score >= 75:
        return "HIGH CONVICTION"

    elif score >= 50:
        return "MODERATE CONVICTION"

    elif score >= 30:
        return "NEUTRAL FLOW"

    return "LOW CONVICTION"


def get_unusual_level(ratio):

    if ratio >= 5:
        return "EXTREME"

    elif ratio >= 3:
        return "HIGH"

    elif ratio >= 1.5:
        return "MODERATE"

    return "NORMAL"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## ⚙️ Scanner Controls")

    available_tickers = sorted(df["Ticker"].unique())

    selected_tickers = st.multiselect(
        "Select Tickers",
        available_tickers,
        default=available_tickers
    )

    minimum_contracts = st.slider(
        "Minimum Contracts",
        min_value=0,
        max_value=10000,
        value=1000,
        step=100
    )

    minimum_premium = st.slider(
        "Minimum Premium ($)",
        min_value=0,
        max_value=5000000,
        value=100000,
        step=50000
    )

    flow_type = st.radio(
        "Flow Type",
        ["All", "CALLS", "PUTS"]
    )

    st.markdown("---")

    scan_button = st.button(
        "🔍 Scan Institutional Flow",
        use_container_width=True
    )


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["Ticker"].isin(selected_tickers)
]

filtered_df = filtered_df[
    filtered_df["Contracts"] >= minimum_contracts
]

filtered_df = filtered_df[
    filtered_df["Premium"] >= minimum_premium
]

if flow_type == "CALLS":

    filtered_df = filtered_df[
        filtered_df["Direction"] == "CALL"
    ]

elif flow_type == "PUTS":

    filtered_df = filtered_df[
        filtered_df["Direction"] == "PUT"
    ]


# ============================================================
# MAIN HEADER
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
# EMPTY RESULT CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "No institutional flow matches the current filters. "
        "Try reducing the Minimum Contracts or Minimum Premium."
    )

    st.stop()


# ============================================================
# SUMMARY METRICS
# ============================================================

bullish_count = len(
    filtered_df[
        filtered_df["Direction"] == "CALL"
    ]
)

bearish_count = len(
    filtered_df[
        filtered_df["Direction"] == "PUT"
    ]
)

call_premium = filtered_df.loc[
    filtered_df["Direction"] == "CALL",
    "Premium"
].sum()

put_premium = filtered_df.loc[
    filtered_df["Direction"] == "PUT",
    "Premium"
].sum()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">
            🟢 Bullish Call Flow
        </div>

        <div class="metric-value metric-green">
            {bullish_count}
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">
            🔴 Bearish Put Flow
        </div>

        <div class="metric-value metric-red">
            {bearish_count}
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">
            💰 Call Premium
        </div>

        <div class="metric-value metric-gold">
            {format_currency(call_premium)}
        </div>
    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">
            💰 Put Premium
        </div>

        <div class="metric-value metric-gold">
            {format_currency(put_premium)}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DIVIDER
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# TOP INSTITUTIONAL FLOW RANKING
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Top Institutional Flow Ranking</div>',
    unsafe_allow_html=True
)


ranking_df = filtered_df.copy()

ranking_df = ranking_df.sort_values(
    by="Score",
    ascending=False
)


display_df = pd.DataFrame()

display_df["Ticker"] = ranking_df["Ticker"]

display_df["Direction"] = ranking_df.apply(
    lambda row:
    "🟢 CALL"
    if row["Direction"] == "CALL"
    else "🔴 PUT",
    axis=1
)

display_df["Activity"] = ranking_df["Activity"]

display_df["Premium"] = ranking_df["Premium"].apply(
    format_currency
)

display_df["Volume Ratio"] = ranking_df[
    "Volume Ratio"
].apply(
    lambda x: f"{x:.1f}x"
)

display_df["Score"] = ranking_df[
    "Score"
].apply(
    lambda x: f"{x}/100"
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DIVIDER
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# FLOW CARD FUNCTION
# ============================================================

def create_flow_card(row):

    ticker = html.escape(str(row["Ticker"]))
    direction = html.escape(str(row["Direction"]))
    activity = html.escape(str(row["Activity"]))
    expiration = html.escape(str(row["Expiration"]))
    transaction = html.escape(str(row["Transaction"]))
    signal = html.escape(str(row["Signal"]))
    unusual_volume = html.escape(str(row["Unusual Volume"]))

    score = int(row["Score"])
    contracts = int(row["Contracts"])
    strike = float(row["Strike"])
    premium = float(row["Premium"])
    volume_ratio = float(row["Volume Ratio"])

    confidence = get_confidence(score)

    if direction == "CALL":

        card_class = "flow-card"
        direction_class = "call-highlight"
        confidence_class = "confidence-call"
        score_class = "score-call"
        value_class = "call-value"

        direction_dot = "🟢"
        transaction_text = "Aggressive Buy"

    else:

        card_class = "flow-card-put"
        direction_class = "put-highlight"
        confidence_class = "confidence-put"
        score_class = "score-put"
        value_class = "put-value"

        direction_dot = "🔴"
        transaction_text = "Aggressive Sell"

    sweep_icon = "⚡" if row["Sweep Detected"] == "YES" else ""
    block_icon = "🧱" if row["Block Trade"] == "YES" else ""

    card_html = f"""
    <div class="{card_class}">

        <div class="flow-card-header">

            <div class="flow-title">
                {direction_dot} {ticker} —
                <span class="{direction_class}">
                    {direction}
                </span>
                BUYING DETECTED
            </div>

        </div>

        <div style="margin-bottom:20px;">

            <span class="{confidence_class}">
                {confidence}
            </span>

            <span class="{score_class}"
                  style="margin-left:15px;">
                Institutional Score: {score}/100
            </span>

        </div>


        <div class="info-grid">


            <div class="info-box">

                <div class="info-label">
                    Institutional Activity
                </div>

                <div class="info-value {value_class}">
                    {activity}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Premium
                </div>

                <div class="info-value">
                    {format_currency(premium)}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Expiration
                </div>

                <div class="info-value">
                    {expiration}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Contracts
                </div>

                <div class="info-value {value_class}">
                    {contracts:,} {direction}S
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Strike
                </div>

                <div class="info-value">
                    ${strike:,.0f}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Volume vs Average
                </div>

                <div class="info-value gold-value">
                    {volume_ratio:.1f}x
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Unusual Volume
                </div>

                <div class="info-value gold-value">
                    {unusual_volume}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Sweep Detected
                </div>

                <div class="info-value">
                    {sweep_icon} {row["Sweep Detected"]}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Block Trade
                </div>

                <div class="info-value">
                    {block_icon} {row["Block Trade"]}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Transaction
                </div>

                <div class="info-value {value_class}">
                    {transaction}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Institutional Signal
                </div>

                <div class="info-value {value_class}">
                    {direction_dot} {signal}
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    Flow Direction
                </div>

                <div class="info-value {value_class}">
                    {direction}
                </div>

            </div>


        </div>

    </div>
    """

    return card_html


# ============================================================
# HIGHEST CONVICTION TRADE
# ============================================================

highest_trade = ranking_df.iloc[0]


st.markdown(
    '<div class="section-title">🔥 Highest Conviction Institutional Trade</div>',
    unsafe_allow_html=True
)


highest_card_html = create_flow_card(highest_trade)

# IMPORTANT:
# This is what fixes the HTML showing as text.
st.markdown(
    highest_card_html,
    unsafe_allow_html=True
)


# ============================================================
# INSTITUTIONAL OPTIONS FLOW ALERTS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


# Get top trades excluding the highest trade
alerts_df = ranking_df.iloc[1:7].copy()


# Display alerts in 2 columns
for i in range(0, len(alerts_df), 2):

    col_left, col_right = st.columns(2)

    # LEFT CARD
    with col_left:

        if i < len(alerts_df):

            row = alerts_df.iloc[i]

            alert_html = create_flow_card(row)

            st.markdown(
                alert_html,
                unsafe_allow_html=True
            )


    # RIGHT CARD
    with col_right:

        if i + 1 < len(alerts_df):

            row = alerts_df.iloc[i + 1]

            alert_html = create_flow_card(row)

            st.markdown(
                alert_html,
                unsafe_allow_html=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        LK Institutional Options Flow Scanner |
        Smart Money Detection System |
        Institutional Flow Analysis
    </div>
    """,
    unsafe_allow_html=True
)
