import streamlit as st
import pandas as pd


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

/* MAIN APP */

.stApp {
    background-color: #151d2b;
    color: #e8edf5;
}


/* HIDE STREAMLIT DEFAULT ELEMENTS */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #253142;
    border-right: 1px solid #39475b;
}

[data-testid="stSidebar"] * {
    color: #e8edf5;
}


/* TITLES */

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

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #f1f3f7;
    margin-top: 30px;
    margin-bottom: 20px;
}


/* METRIC CARDS */

[data-testid="stMetric"] {
    background: #222d3d;
    border: 1px solid #35445a;
    border-radius: 16px;
    padding: 20px;
    min-height: 115px;
}

[data-testid="stMetricLabel"] {
    color: #aeb7c5 !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #f3f5f8 !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}


/* DIVIDER */

.custom-divider {
    border-top: 1px solid #344052;
    margin-top: 45px;
    margin-bottom: 40px;
}


/* FLOW CARD */

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
}


/* BUTTON */

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


/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
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
# SIDEBAR
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

scan_button = st.sidebar.button(
    "🔍 Scan Institutional Flow"
)


# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = df.copy()


if selected_tickers:

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
    ascending=False
).reset_index(drop=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📊 LK Institutional Options Flow Scanner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Money Detection • Institutional Options Activity • High Conviction Flow Analysis</div>',
    unsafe_allow_html=True
)


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


# =========================================================
# NATIVE STREAMLIT METRIC CARDS
# FIXED VERSION - NO HTML RENDERING PROBLEM
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        label="🟢 BULLISH CALL FLOW",
        value=bullish_count
    )


with col2:
    st.metric(
        label="🔴 BEARISH PUT FLOW",
        value=bearish_count
    )


with col3:
    st.metric(
        label="💰 CALL PREMIUM",
        value=f"${call_premium:,.0f}"
    )


with col4:
    st.metric(
        label="💰 PUT PREMIUM",
        value=f"${put_premium:,.0f}"
    )


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
# CONFIDENCE FUNCTION
# =========================================================

def get_confidence(score):

    if score >= 90:
        return "🔥 EXTREME INSTITUTIONAL FLOW"

    elif score >= 75:
        return "🟢 HIGH CONVICTION"

    elif score >= 50:
        return "🟡 MODERATE CONVICTION"

    elif score >= 30:
        return "🟣 NEUTRAL FLOW"

    else:
        return "🔵 LOW CONVICTION"


# =========================================================
# DISPLAY FLOW CARD
# =========================================================

def display_flow_card(trade):

    direction = trade["direction"]
    score = int(trade["score"])


    if direction == "CALL":

        border_color = "#58d69b"
        direction_icon = "🟢"
        direction_color = "#62d69d"

    else:

        border_color = "#ff5964"
        direction_icon = "🔴"
        direction_color = "#ff737d"


    # =====================================================
    # FLOW CARD CONTAINER
    # =====================================================

    with st.container(border=True):


        # =================================================
        # CARD HEADER
        # =================================================

        col_title, col_confidence = st.columns([3, 1])


        with col_title:

            st.markdown(
                f"## {direction_icon} {trade['ticker']} —"
            )

            st.markdown(
                f'<span style="color:{direction_color}; font-weight:700;">{direction}</span>',
                unsafe_allow_html=True
            )

            st.caption("BUYING DETECTED")


        with col_confidence:

            confidence = get_confidence(score)

            st.markdown(
                f"""
<div style="
padding:10px;
border-radius:10px;
text-align:center;
font-weight:700;
color:{direction_color};
border:1px solid {border_color};
background:rgba(255,255,255,0.04);
margin-top:10px;
">
{confidence}
</div>
""",
                unsafe_allow_html=True
            )


        st.markdown("---")


        # =================================================
        # ROW 1
        # =================================================

        c1, c2, c3 = st.columns(3)


        with c1:
            st.caption("Institutional Activity")
            st.markdown(f"**{trade['activity']}**")


        with c2:
            st.caption("Institutional Score")
            st.markdown(f"**{score}/100**")


        with c3:
            st.caption("Expiration")
            st.markdown(f"**{trade['expiration']}**")


        # =================================================
        # ROW 2
        # =================================================

        c4, c5, c6 = st.columns(3)


        with c4:
            st.caption("Contracts")
            st.markdown(
                f"**{trade['contracts']:,} {direction}S**"
            )


        with c5:
            st.caption("Strike")
            st.markdown(
                f"**${trade['strike']:,.0f}**"
            )


        with c6:
            st.caption("Premium")
            st.markdown(
                f"**${trade['premium']:,.0f}**"
            )


        # =================================================
        # ROW 3
        # =================================================

        c7, c8, c9 = st.columns(3)


        with c7:
            st.caption("Volume vs Average")
            st.markdown(
                f"**{trade['volume_ratio']:.1f}x**"
            )


        with c8:
            st.caption("Unusual Volume")
            st.markdown(
                f"**{trade['unusual_volume']}**"
            )


        with c9:

            st.caption("Sweep Detected")

            if trade["sweep"] == "YES":
                st.markdown("**⚡ YES**")
            else:
                st.markdown("**NO**")


        # =================================================
        # ROW 4
        # =================================================

        c10, c11, c12 = st.columns(3)


        with c10:

            st.caption("Block Trade")

            if trade["block_trade"] == "YES":
                st.markdown("**🧱 YES**")
            else:
                st.markdown("**NO**")


        with c11:

            st.caption("Transaction")

            st.markdown(
                f"**{trade['transaction']}**"
            )


        with c12:

            st.caption("Signal")

            st.markdown(
                f"**{direction_icon} {trade['signal']}**"
            )


        st.markdown("---")


        # =================================================
        # FINAL SIGNAL
        # =================================================

        st.markdown(
            f"""
Institutional Smart Money Signal:
<span style="
color:{direction_color};
font-weight:700;
">
{trade['signal']}
</span>
""",
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

display_flow_card(highest_trade)


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


remaining_trades = filtered_df.iloc[1:]


for index in range(0, len(remaining_trades), 2):


    col_left, col_right = st.columns(2)


    with col_left:

        trade = remaining_trades.iloc[index]

        display_flow_card(trade)


    if index + 1 < len(remaining_trades):

        with col_right:

            trade = remaining_trades.iloc[index + 1]

            display_flow_card(trade)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div style="
text-align:center;
color:#718096;
padding:30px;
font-size:14px;
">
LK Institutional Options Flow Scanner
• Smart Money Detection Engine
</div>
""",
    unsafe_allow_html=True
)
