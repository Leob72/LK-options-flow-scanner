import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER v1.0
# Smart Money Detection Dashboard
# ============================================================

st.set_page_config(
    page_title="LK Institutional Options Flow Scanner",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------------
# CUSTOM STYLE
# ------------------------------------------------------------

st.markdown("""
<style>

    .main {
        background-color: #0E1117;
    }

    .title {
        font-size: 38px;
        font-weight: 700;
        color: white;
    }

    .subtitle {
        font-size: 18px;
        color: #A0A0A0;
    }

    .call-box {
        background-color: #123D2A;
        border-left: 6px solid #00C853;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    .put-box {
        background-color: #421C24;
        border-left: 6px solid #FF3B4D;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    .metric-label {
        color: #A0A0A0;
        font-size: 14px;
    }

    .metric-value {
        color: white;
        font-size: 22px;
        font-weight: bold;
    }
.metric-value {
    color: white;
    font-size: 22px;
    font-weight: bold;
}


/* BULLISH - CALL */
.bullish-alert, .bullish-card {
    color: #FFFFFF !important;
}

.bullish-alert h1, .bullish-alert h2, .bullish-alert h3,
.bullish-card h1, .bullish-card h2, .bullish-card h3 {
    color: #00ff00 !important;
}

.bullish-alert p, .bullish-alert div, .bullish-alert span,
.bullish-card p, .bullish-card div, .bullish-card span {
    color: #FFFFFF !important;
}


/* BEARISH - PUT */
.bearish-alert, .bearish-card {
    color: #FFFFFF !important;
}

.bearish-alert h1, .bearish-alert h2, .bearish-alert h3,
.bearish-card h1, .bearish-card h2, .bearish-card h3 {
    color: #ff0000 !important;
}

.bearish-alert p, .bearish-alert div, .bearish-alert span,
.bearish-card p, .bearish-card div, .bearish-card span {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

st.markdown(
    '<div class="title">LK Institutional Options Flow Scanner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Money • Unusual Options Activity • Institutional Flow Detection</div>',
    unsafe_allow_html=True
)

st.divider()


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.header("⚙️ Scanner Controls")

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

min_contracts = st.sidebar.slider(
    "Minimum Contracts",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)

min_premium = st.sidebar.slider(
    "Minimum Premium ($)",
    min_value=100000,
    max_value=10000000,
    value=1000000,
    step=100000
)

flow_filter = st.sidebar.radio(
    "Flow Type",
    ["ALL", "CALLS", "PUTS"]
)

st.sidebar.divider()

st.sidebar.markdown("### Scanner Status")
st.sidebar.success("● SYSTEM READY")
st.sidebar.caption("Demo Mode - Live Data API Coming Next")


# ------------------------------------------------------------
# DEMO DATA
# ------------------------------------------------------------

today = datetime.now().date()

data = [
    {
        "Ticker": "AAPL",
        "Type": "CALL",
        "Contracts": 2500,
        "Expiration": today + timedelta(days=4),
        "Strike": 325,
        "Premium": 1800000,
        "Flow": "Aggressive Buy",
        "Sentiment": "BULLISH"
    },
    {
        "Ticker": "NVDA",
        "Type": "PUT",
        "Contracts": 4200,
        "Expiration": today + timedelta(days=7),
        "Strike": 175,
        "Premium": 3200000,
        "Flow": "Aggressive Buy",
        "Sentiment": "BEARISH"
    },
    {
        "Ticker": "TSLA",
        "Type": "CALL",
        "Contracts": 1800,
        "Expiration": today + timedelta(days=11),
        "Strike": 350,
        "Premium": 2100000,
        "Flow": "Sweep",
        "Sentiment": "BULLISH"
    },
    {
        "Ticker": "PLTR",
        "Type": "CALL",
        "Contracts": 5200,
        "Expiration": today + timedelta(days=6),
        "Strike": 180,
        "Premium": 2900000,
        "Flow": "Block Trade",
        "Sentiment": "BULLISH"
    },
    {
        "Ticker": "META",
        "Type": "PUT",
        "Contracts": 3100,
        "Expiration": today + timedelta(days=14),
        "Strike": 720,
        "Premium": 4100000,
        "Flow": "Sweep",
        "Sentiment": "BEARISH"
    },
    {
        "Ticker": "AMZN",
        "Type": "CALL",
        "Contracts": 3600,
        "Expiration": today + timedelta(days=8),
        "Strike": 265,
        "Premium": 2500000,
        "Flow": "Aggressive Buy",
        "Sentiment": "BULLISH"
    },
    {
        "Ticker": "QQQ",
        "Type": "PUT",
        "Contracts": 6000,
        "Expiration": today + timedelta(days=5),
        "Strike": 590,
        "Premium": 5200000,
        "Flow": "Block Trade",
        "Sentiment": "BEARISH"
    },
    {
        "Ticker": "SPY",
        "Type": "CALL",
        "Contracts": 7500,
        "Expiration": today + timedelta(days=3),
        "Strike": 650,
        "Premium": 6800000,
        "Flow": "Sweep",
        "Sentiment": "BULLISH"
    }
]

df = pd.DataFrame(data)


# ------------------------------------------------------------
# FILTERS
# ------------------------------------------------------------

df_filtered = df.copy()

df_filtered = df_filtered[
    df_filtered["Ticker"].isin(selected_tickers)
]

df_filtered = df_filtered[
    df_filtered["Contracts"] >= min_contracts
]

df_filtered = df_filtered[
    df_filtered["Premium"] >= min_premium
]

if flow_filter == "CALLS":
    df_filtered = df_filtered[df_filtered["Type"] == "CALL"]

elif flow_filter == "PUTS":
    df_filtered = df_filtered[df_filtered["Type"] == "PUT"]


# ------------------------------------------------------------
# TOP METRICS
# ------------------------------------------------------------

calls = len(df_filtered[df_filtered["Type"] == "CALL"])
puts = len(df_filtered[df_filtered["Type"] == "PUT"])

call_premium = df_filtered[
    df_filtered["Type"] == "CALL"
]["Premium"].sum()

put_premium = df_filtered[
    df_filtered["Type"] == "PUT"
]["Premium"].sum()


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🟢 BULLISH CALL FLOW",
    calls
)

col2.metric(
    "🔴 BEARISH PUT FLOW",
    puts
)

col3.metric(
    "💰 CALL PREMIUM",
    f"${call_premium:,.0f}"
)

col4.metric(
    "💰 PUT PREMIUM",
    f"${put_premium:,.0f}"
)


st.divider()


# ------------------------------------------------------------
# SMART MONEY SIGNALS
# ------------------------------------------------------------

st.subheader("🚨 Institutional Options Flow Alerts")

if len(df_filtered) == 0:

    st.warning("No unusual options activity detected with current filters.")

else:

    for _, row in df_filtered.iterrows():

        if row["Type"] == "CALL":

            st.markdown(
                f"""
                <div class="call-box">

                <h3>🟢 {row["Ticker"]} — CALL BUYING DETECTED</h3>

                <p>
                <b>Expiration:</b> {row["Expiration"].strftime("%b %d")}<br>
                <b>Contracts:</b> {row["Contracts"]:,} CALLS<br>
                <b>Strike:</b> ${row["Strike"]}<br>
                <b>Premium:</b> ${row["Premium"]:,.0f}<br>
                <b>Type:</b> {row["Flow"]}<br>
                <b>Signal:</b> 🟢 Bullish Institutional Flow
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="put-box">

                <h3>🔴 {row["Ticker"]} — PUT BUYING DETECTED</h3>

                <p>
                <b>Expiration:</b> {row["Expiration"].strftime("%b %d")}<br>
                <b>Contracts:</b> {row["Contracts"]:,} PUTS<br>
                <b>Strike:</b> ${row["Strike"]}<br>
                <b>Premium:</b> ${row["Premium"]:,.0f}<br>
                <b>Type:</b> {row["Flow"]}<br>
                <b>Signal:</b> 🔴 Bearish Institutional Flow
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


# ------------------------------------------------------------
# DATA TABLE
# ------------------------------------------------------------

st.divider()

st.subheader("📊 Smart Money Flow Table")

display_df = df_filtered.copy()

display_df["Premium"] = display_df["Premium"].apply(
    lambda x: f"${x:,.0f}"
)

display_df["Expiration"] = display_df["Expiration"].apply(
    lambda x: x.strftime("%Y-%m-%d")
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# MARKET SENTIMENT
# ------------------------------------------------------------

st.divider()

st.subheader("🧠 Institutional Sentiment")

if call_premium > put_premium:
    st.success(
        "🟢 MARKET FLOW BIAS: BULLISH — Institutional CALL premium is dominating."
    )

elif put_premium > call_premium:
    st.error(
        "🔴 MARKET FLOW BIAS: BEARISH — Institutional PUT premium is dominating."
    )

else:
    st.info(
        "🟡 MARKET FLOW BIAS: NEUTRAL — CALL and PUT flow is balanced."
    )


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.divider()

st.caption(
    "LK Institutional Options Flow Scanner v1.0 | "
    "Smart Money Detection Dashboard | Demo Version"
)
