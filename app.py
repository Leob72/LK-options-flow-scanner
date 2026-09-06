import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

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
.main {
    background-color: #0E1117;
}


/* TITLE */
.title {
    font-size: 38px;
    font-weight: 700;
    color: white;
}


/* SUBTITLE */
.subtitle {
    font-size: 18px;
    color: #A0A0A0;
}


/* CALL ALERT BOX */
.call-box {
    background-color: #123D2A;
    border-left: 6px solid #00ff00;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
    color: white !important;
}


/* PUT ALERT BOX */
.put-box {
    background-color: #421C24;
    border-left: 6px solid #ff0000;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
    color: white !important;
}


/* METRIC LABEL */
.metric-label {
    color: #A0A0A0;
    font-size: 14px;
}


/* METRIC VALUE */
.metric-value {
    color: white;
    font-size: 22px;
    font-weight: bold;
}


/* ============================================================
   BULLISH - CALL TEXT COLORS
   ============================================================ */

.bullish-alert,
.bullish-card {
    color: white !important;
}

.bullish-alert h1,
.bullish-alert h2,
.bullish-alert h3,
.bullish-alert h4,
.bullish-card h1,
.bullish-card h2,
.bullish-card h3,
.bullish-card h4 {
    color: #00ff00 !important;
}

.bullish-alert p,
.bullish-alert div,
.bullish-alert span,
.bullish-card p,
.bullish-card div,
.bullish-card span {
    color: white !important;
}


/* ============================================================
   BEARISH - PUT TEXT COLORS
   ============================================================ */

.bearish-alert,
.bearish-card {
    color: white !important;
}

.bearish-alert h1,
.bearish-alert h2,
.bearish-alert h3,
.bearish-alert h4,
.bearish-card h1,
.bearish-card h2,
.bearish-card h3,
.bearish-card h4 {
    color: #ff0000 !important;
}

.bearish-alert p,
.bearish-alert div,
.bearish-alert span,
.bearish-card p,
.bearish-card div,
.bearish-card span {
    color: white !important;
}


/* BULLISH DOT */
.bullish-dot {
    color: #00ff00 !important;
}


/* BEARISH DOT */
.bearish-dot {
    color: #ff0000 !important;
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

# Esta sección puede conectarse posteriormente a una API real.
# Por ahora mantiene la estructura del scanner.

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
    "## 🚨 Institutional Options Flow Alerts"
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

            st.markdown(
                f"""
                <div class="call-box bullish-alert">

                    <h2>
                        🟢 {item["ticker"]} —
                        <span style="color:#00ff00 !important;">
                        CALL
                        </span>
                        BUYING DETECTED
                    </h2>

                    <p>
                        <b>Expiration:</b>
                        {item["expiration"]}
                    </p>

                    <p>
                        <b>Contracts:</b>
                        {item["contracts"]:,}
                        <span style="color:#00ff00 !important;">
                        CALLS
                        </span>
                    </p>

                    <p>
                        <b>Strike:</b>
                        ${item["strike"]}
                    </p>

                    <p>
                        <b>Premium:</b>
                        ${item["premium"]:,.0f}
                    </p>

                    <p>
                        <b>Type:</b>
                        Aggressive Buy
                    </p>

                    <p>
                        <b>Signal:</b>
                        <span style="color:#00ff00 !important;">
                        🟢 {item["signal"]}
                        </span>
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # BEARISH PUT
        # ====================================================

        elif item["type"] == "PUT":

            st.markdown(
                f"""
                <div class="put-box bearish-alert">

                    <h2>
                        🔴 {item["ticker"]} —
                        <span style="color:#ff0000 !important;">
                        PUT
                        </span>
                        BUYING DETECTED
                    </h2>

                    <p>
                        <b>Expiration:</b>
                        {item["expiration"]}
                    </p>

                    <p>
                        <b>Contracts:</b>
                        {item["contracts"]:,}
                        <span style="color:#ff0000 !important;">
                        PUTS
                        </span>
                    </p>

                    <p>
                        <b>Strike:</b>
                        ${item["strike"]}
                    </p>

                    <p>
                        <b>Premium:</b>
                        ${item["premium"]:,.0f}
                    </p>

                    <p>
                        <b>Type:</b>
                        Aggressive Buy
                    </p>

                    <p>
                        <b>Signal:</b>
                        <span style="color:#ff0000 !important;">
                        🔴 {item["signal"]}
                        </span>
                    </p>

                </div>
                """,
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
