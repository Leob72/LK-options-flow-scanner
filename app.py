import streamlit as st
import pandas as pd

# ============================================================
# LK INSTITUTIONAL OPTIONS FLOW SCANNER v3.0
# SMART MONEY INTELLIGENCE ENGINE
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

/* MAIN APP */
.stApp {
    background-color: #11151D;
    color: #E8E8E8;
}

/* MAIN CONTENT */
.main {
    background-color: #11151D;
}

/* TITLE */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #F2F2F2;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 17px;
    color: #9AA4B2;
    margin-bottom: 25px;
}

/* SECTION TITLES */
.section-title {
    font-size: 30px;
    font-weight: 750;
    color: #F2F2F2;
    margin-top: 20px;
    margin-bottom: 18px;
}

/* PRIORITY ALERT */
.priority-bullish {
    background: linear-gradient(90deg, #123D2A, #183F30);
    border-left: 7px solid #00E676;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
}

.priority-bearish {
    background: linear-gradient(90deg, #421C24, #4A2028);
    border-left: 7px solid #FF1744;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
}

/* CALL ALERT BOX */
.call-box {
    background-color: #153D2B;
    border-left: 7px solid #00E676;
    padding: 26px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: #E8E8E8 !important;
}

/* PUT ALERT BOX */
.put-box {
    background-color: #482127;
    border-left: 7px solid #FF1744;
    padding: 26px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: #E8E8E8 !important;
}

/* CARD HEADERS */
.call-box h2,
.put-box h2,
.priority-bullish h2,
.priority-bearish h2 {
    color: #F2F2F2 !important;
    font-size: 32px !important;
    margin-bottom: 20px !important;
}

/* TEXT */
.call-box p,
.put-box p,
.priority-bullish p,
.priority-bearish p {
    color: #D8D8D8 !important;
    font-size: 18px;
    margin-bottom: 13px;
}

/* BULLISH TEXT */
.bullish {
    color: #39E58C !important;
    font-weight: 750;
}

/* BEARISH TEXT */
.bearish {
    color: #FF4562 !important;
    font-weight: 750;
}

/* GOLD TEXT */
.gold {
    color: #FFD54A !important;
    font-weight: 750;
}

/* WHITE BOLD */
.label {
    color: #E8E8E8 !important;
    font-weight: 700;
}

/* SUMMARY BOX */
.summary-box {
    background-color: #1A202B;
    border: 1px solid #303A48;
    border-radius: 12px;
    padding: 25px;
    margin-top: 15px;
    margin-bottom: 20px;
}

.summary-box p {
    color: #D8D8D8 !important;
    font-size: 18px;
    line-height: 1.6;
}

/* RANKING TABLE */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #171C25;
}

/* METRICS */
[data-testid="stMetric"] {
    background-color: #1A202B;
    border: 1px solid #2D3745;
    padding: 15px;
    border-radius: 10px;
}

/* DIVIDER */
hr {
    border-color: #2D3745 !important;
}

/* FOOTER */
.footer {
    color: #7F8A99;
    text-align: center;
    padding: 20px;
    font-size: 14px;
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
    '<div class="subtitle">Smart Money Intelligence Engine • Institutional Options Activity Analysis</div>',
    unsafe_allow_html=True
)

st.divider()


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
# FUTURE: REPLACE WITH REAL API DATA
# ============================================================

sample_data = [

    {
        "ticker": "AAPL",
        "type": "CALL",
        "expiration": "Sep 10",
        "contracts": 2500,
        "strike": 325,
        "premium": 1800000,
        "volume_ratio": 5.6,
        "sweep": True,
        "block_trade": False,
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "NVDA",
        "type": "PUT",
        "expiration": "Sep 13",
        "contracts": 4200,
        "strike": 175,
        "premium": 3200000,
        "volume_ratio": 7.0,
        "sweep": False,
        "block_trade": True,
        "transaction": "Aggressive Sell"
    },

    {
        "ticker": "TSLA",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 1800,
        "strike": 350,
        "premium": 1450000,
        "volume_ratio": 2.0,
        "sweep": False,
        "block_trade": False,
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "QQQ",
        "type": "PUT",
        "expiration": "Sep 10",
        "contracts": 3100,
        "strike": 580,
        "premium": 2200000,
        "volume_ratio": 6.2,
        "sweep": True,
        "block_trade": False,
        "transaction": "Aggressive Sell"
    },

    {
        "ticker": "META",
        "type": "CALL",
        "expiration": "Sep 13",
        "contracts": 3600,
        "strike": 750,
        "premium": 3900000,
        "volume_ratio": 9.0,
        "sweep": True,
        "block_trade": False,
        "transaction": "Aggressive Buy"
    },

    {
        "ticker": "PLTR",
        "type": "CALL",
        "expiration": "Sep 20",
        "contracts": 1100,
        "strike": 200,
        "premium": 650000,
        "volume_ratio": 1.4,
        "sweep": False,
        "block_trade": False,
        "transaction": "Neutral"
    }

]


# ============================================================
# INSTITUTIONAL SCORE ENGINE
# ============================================================

def calculate_institutional_score(item):

    score = 0

    # --------------------------------------------------------
    # PREMIUM SCORE - MAX 30
    # --------------------------------------------------------

    premium = item["premium"]

    if premium >= 3000000:
        score += 30
    elif premium >= 2000000:
        score += 25
    elif premium >= 1000000:
        score += 20
    elif premium >= 500000:
        score += 12
    else:
        score += 5


    # --------------------------------------------------------
    # VOLUME RATIO SCORE - MAX 25
    # --------------------------------------------------------

    ratio = item["volume_ratio"]

    if ratio >= 7:
        score += 25
    elif ratio >= 5:
        score += 20
    elif ratio >= 3:
        score += 15
    elif ratio >= 2:
        score += 10
    else:
        score += 5


    # --------------------------------------------------------
    # CONTRACT SIZE - MAX 15
    # --------------------------------------------------------

    contracts = item["contracts"]

    if contracts >= 4000:
        score += 15
    elif contracts >= 3000:
        score += 12
    elif contracts >= 2000:
        score += 10
    elif contracts >= 1000:
        score += 6
    else:
        score += 3


    # --------------------------------------------------------
    # SWEEP DETECTION - MAX 15
    # --------------------------------------------------------

    if item["sweep"]:
        score += 15


    # --------------------------------------------------------
    # BLOCK TRADE - MAX 10
    # --------------------------------------------------------

    if item["block_trade"]:
        score += 10


    # --------------------------------------------------------
    # AGGRESSIVE TRANSACTION - MAX 5
    # --------------------------------------------------------

    if item["transaction"] in ["Aggressive Buy", "Aggressive Sell"]:
        score += 5


    return min(score, 100)


# ============================================================
# CONFIDENCE ENGINE
# ============================================================

def get_confidence(score):

    if score >= 90:
        return "EXTREME INSTITUTIONAL FLOW"

    elif score >= 75:
        return "HIGH CONVICTION"

    elif score >= 55:
        return "STRONG FLOW"

    elif score >= 35:
        return "MODERATE FLOW"

    else:
        return "LOW CONVICTION"


# ============================================================
# UNUSUAL VOLUME ENGINE
# ============================================================

def get_unusual_volume(ratio):

    if ratio >= 5:
        return "EXTREME"

    elif ratio >= 3:
        return "HIGH"

    elif ratio >= 2:
        return "MODERATE"

    else:
        return "NORMAL"


# ============================================================
# ACTIVITY CLASSIFICATION
# ============================================================

def get_activity(item):

    if item["block_trade"]:
        return "BLOCK TRADE"

    elif item["sweep"]:
        return "SWEEP"

    else:
        return "STANDARD FLOW"


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


    # CREATE COPY
    processed_item = item.copy()

    processed_item["score"] = calculate_institutional_score(item)
    processed_item["confidence"] = get_confidence(
        processed_item["score"]
    )
    processed_item["unusual_volume"] = get_unusual_volume(
        item["volume_ratio"]
    )
    processed_item["activity"] = get_activity(item)

    if item["type"] == "CALL":
        processed_item["signal"] = "Bullish Institutional Flow"
    else:
        processed_item["signal"] = "Bearish Institutional Flow"

    filtered_data.append(processed_item)


# ============================================================
# SORT BY INSTITUTIONAL SCORE
# ============================================================

filtered_data = sorted(
    filtered_data,
    key=lambda x: x["score"],
    reverse=True
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if len(filtered_data) == 0:

    st.warning(
        "⚠️ No institutional options flow detected based on current filters."
    )

    st.stop()


# ============================================================
# MARKET SENTIMENT CALCULATIONS
# ============================================================

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

total_premium = call_premium + put_premium


if total_premium > 0:

    bullish_percentage = (
        call_premium / total_premium
    ) * 100

    bearish_percentage = (
        put_premium / total_premium
    ) * 100

else:

    bullish_percentage = 0
    bearish_percentage = 0


if bullish_percentage >= 60:
    market_bias = "BULLISH"

elif bearish_percentage >= 60:
    market_bias = "BEARISH"

else:
    market_bias = "NEUTRAL"


# ============================================================
# MARKET SENTIMENT DASHBOARD
# ============================================================

st.markdown(
    '<div class="section-title">📊 Institutional Market Sentiment</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "🟢 CALL PREMIUM",
        f"${call_premium:,.0f}"
    )

with col2:

    st.metric(
        "🔴 PUT PREMIUM",
        f"${put_premium:,.0f}"
    )

with col3:

    st.metric(
        "🟢 BULLISH FLOW",
        f"{bullish_percentage:.1f}%"
    )

with col4:

    st.metric(
        "🔴 BEARISH FLOW",
        f"{bearish_percentage:.1f}%"
    )


st.write("")

# MARKET BIAS

if market_bias == "BULLISH":

    st.success(
        f"📈 Institutional Market Bias: {market_bias}"
    )

elif market_bias == "BEARISH":

    st.error(
        f"📉 Institutional Market Bias: {market_bias}"
    )

else:

    st.info(
        f"⚖️ Institutional Market Bias: {market_bias}"
    )


st.divider()


# ============================================================
# TOP PRIORITY ALERT
# ============================================================

top_trade = filtered_data[0]

st.markdown(
    '<div class="section-title">🔥 Highest Conviction Institutional Trade</div>',
    unsafe_allow_html=True
)


if top_trade["type"] == "CALL":

    st.markdown(
        f"""
        <div class="priority-bullish">

            <h2>
                🟢 {top_trade["ticker"]} —
                <span class="bullish">
                CALL
                </span>
                BUYING DETECTED
            </h2>

            <p>
                <span class="label">Institutional Score:</span>
                <span class="bullish">
                {top_trade["score"]}/100
                </span>
            </p>

            <p>
                <span class="label">Confidence:</span>
                <span class="bullish">
                {top_trade["confidence"]}
                </span>
            </p>

            <p>
                <span class="label">Institutional Activity:</span>
                <span class="bullish">
                {top_trade["activity"]}
                </span>
            </p>

            <p>
                <span class="label">Premium:</span>
                ${top_trade["premium"]:,.0f}
            </p>

            <p>
                <span class="label">Volume vs Average:</span>
                <span class="gold">
                {top_trade["volume_ratio"]:.1f}x
                </span>
            </p>

            <p>
                <span class="label">Signal:</span>
                <span class="bullish">
                🟢 {top_trade["signal"]}
                </span>
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


else:

    st.markdown(
        f"""
        <div class="priority-bearish">

            <h2>
                🔴 {top_trade["ticker"]} —
                <span class="bearish">
                PUT
                </span>
                BUYING DETECTED
            </h2>

            <p>
                <span class="label">Institutional Score:</span>
                <span class="bearish">
                {top_trade["score"]}/100
                </span>
            </p>

            <p>
                <span class="label">Confidence:</span>
                <span class="bearish">
                {top_trade["confidence"]}
                </span>
            </p>

            <p>
                <span class="label">Institutional Activity:</span>
                <span class="bearish">
                {top_trade["activity"]}
                </span>
            </p>

            <p>
                <span class="label">Premium:</span>
                ${top_trade["premium"]:,.0f}
            </p>

            <p>
                <span class="label">Volume vs Average:</span>
                <span class="gold">
                {top_trade["volume_ratio"]:.1f}x
                </span>
            </p>

            <p>
                <span class="label">Signal:</span>
                <span class="bearish">
                🔴 {top_trade["signal"]}
                </span>
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# TOP INSTITUTIONAL FLOW RANKING
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Top Institutional Flow Ranking</div>',
    unsafe_allow_html=True
)


ranking_data = []

for item in filtered_data:

    if item["type"] == "CALL":
        direction = "🟢 CALL"
    else:
        direction = "🔴 PUT"

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


st.divider()


# ============================================================
# DETAILED INSTITUTIONAL ALERTS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Institutional Options Flow Alerts</div>',
    unsafe_allow_html=True
)


for item in filtered_data:

    # ========================================================
    # CALL
    # ========================================================

    if item["type"] == "CALL":

        sweep_text = (
            "⚡ YES"
            if item["sweep"]
            else "NO"
        )

        block_text = (
            "🧱 YES"
            if item["block_trade"]
            else "NO"
        )

        st.markdown(
            f"""
            <div class="call-box">

                <h2>
                    🟢 {item["ticker"]} —
                    <span class="bullish">
                    CALL
                    </span>
                    BUYING DETECTED
                </h2>

                <p>
                    <span class="label">Institutional Activity:</span>
                    <span class="bullish">
                    {item["activity"]}
                    </span>
                </p>

                <p>
                    <span class="label">Institutional Score:</span>
                    <span class="bullish">
                    {item["score"]}/100
                    </span>
                </p>

                <p>
                    <span class="label">Confidence:</span>
                    <span class="bullish">
                    {item["confidence"]}
                    </span>
                </p>

                <p>
                    <span class="label">Expiration:</span>
                    {item["expiration"]}
                </p>

                <p>
                    <span class="label">Contracts:</span>
                    {item["contracts"]:,}
                    <span class="bullish">
                    CALLS
                    </span>
                </p>

                <p>
                    <span class="label">Strike:</span>
                    ${item["strike"]}
                </p>

                <p>
                    <span class="label">Premium:</span>
                    ${item["premium"]:,.0f}
                </p>

                <p>
                    <span class="label">Volume vs Average:</span>
                    <span class="gold">
                    {item["volume_ratio"]:.1f}x
                    </span>
                </p>

                <p>
                    <span class="label">Unusual Volume:</span>
                    <span class="gold">
                    {item["unusual_volume"]}
                    </span>
                </p>

                <p>
                    <span class="label">Sweep Detected:</span>
                    {sweep_text}
                </p>

                <p>
                    <span class="label">Block Trade:</span>
                    {block_text}
                </p>

                <p>
                    <span class="label">Transaction:</span>
                    <span class="bullish">
                    {item["transaction"]}
                    </span>
                </p>

                <p>
                    <span class="label">Signal:</span>
                    <span class="bullish">
                    🟢 {item["signal"]}
                    </span>
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # PUT
    # ========================================================

    else:

        sweep_text = (
            "⚡ YES"
            if item["sweep"]
            else "NO"
        )

        block_text = (
            "🧱 YES"
            if item["block_trade"]
            else "NO"
        )

        st.markdown(
            f"""
            <div class="put-box">

                <h2>
                    🔴 {item["ticker"]} —
                    <span class="bearish">
                    PUT
                    </span>
                    BUYING DETECTED
                </h2>

                <p>
                    <span class="label">Institutional Activity:</span>
                    <span class="bearish">
                    {item["activity"]}
                    </span>
                </p>

                <p>
                    <span class="label">Institutional Score:</span>
                    <span class="bearish">
                    {item["score"]}/100
                    </span>
                </p>

                <p>
                    <span class="label">Confidence:</span>
                    <span class="bearish">
                    {item["confidence"]}
                    </span>
                </p>

                <p>
                    <span class="label">Expiration:</span>
                    {item["expiration"]}
                </p>

                <p>
                    <span class="label">Contracts:</span>
                    {item["contracts"]:,}
                    <span class="bearish">
                    PUTS
                    </span>
                </p>

                <p>
                    <span class="label">Strike:</span>
                    ${item["strike"]}
                </p>

                <p>
                    <span class="label">Premium:</span>
                    ${item["premium"]:,.0f}
                </p>

                <p>
                    <span class="label">Volume vs Average:</span>
                    <span class="gold">
                    {item["volume_ratio"]:.1f}x
                    </span>
                </p>

                <p>
                    <span class="label">Unusual Volume:</span>
                    <span class="gold">
                    {item["unusual_volume"]}
                    </span>
                </p>

                <p>
                    <span class="label">Sweep Detected:</span>
                    {sweep_text}
                </p>

                <p>
                    <span class="label">Block Trade:</span>
                    {block_text}
                </p>

                <p>
                    <span class="label">Transaction:</span>
                    <span class="bearish">
                    {item["transaction"]}
                    </span>
                </p>

                <p>
                    <span class="label">Signal:</span>
                    <span class="bearish">
                    🔴 {item["signal"]}
                    </span>
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SMART MONEY SUMMARY
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🧠 Smart Money Intelligence Summary</div>',
    unsafe_allow_html=True
)


# GET TOP CALLS AND PUTS

top_calls = [
    x for x in filtered_data
    if x["type"] == "CALL"
]

top_puts = [
    x for x in filtered_data
    if x["type"] == "PUT"
]


call_names = ", ".join(
    [x["ticker"] for x in top_calls[:3]]
)

put_names = ", ".join(
    [x["ticker"] for x in top_puts[:3]]
)


# CREATE SUMMARY

if market_bias == "BULLISH":

    summary = f"""
    Institutional options activity currently shows a
    <span class="bullish">BULLISH MARKET BIAS</span>.

    CALL premium represents
    <span class="bullish">{bullish_percentage:.1f}%</span>
    of detected institutional flow.

    The strongest bullish positioning is concentrated in
    <span class="bullish">{call_names if call_names else "selected CALL contracts"}</span>.

    Bearish positioning remains present through
    <span class="bearish">{put_names if put_names else "PUT activity"}</span>,
    suggesting selective hedging or bearish speculation.
    """

elif market_bias == "BEARISH":

    summary = f"""
    Institutional options activity currently shows a
    <span class="bearish">BEARISH MARKET BIAS</span>.

    PUT premium represents
    <span class="bearish">{bearish_percentage:.1f}%</span>
    of detected institutional flow.

    The strongest bearish positioning is concentrated in
    <span class="bearish">{put_names if put_names else "selected PUT contracts"}</span>.

    Bullish positioning remains present through
    <span class="bullish">{call_names if call_names else "CALL activity"}</span>,
    suggesting selective upside speculation or hedging.
    """

else:

    summary = f"""
    Institutional options activity currently shows a
    <span class="gold">NEUTRAL MARKET BIAS</span>.

    CALL premium represents
    <span class="bullish">{bullish_percentage:.1f}%</span>
    of institutional flow while PUT premium represents
    <span class="bearish">{bearish_percentage:.1f}%</span>.

    The institutional market is showing mixed positioning,
    suggesting that smart money is selectively positioning
    rather than expressing a strong directional bias.
    """


st.markdown(
    f"""
    <div class="summary-box">
        <p>{summary}</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        LK Institutional Options Flow Scanner v3.0<br>
        Smart Money Intelligence Engine • Institutional Flow Analytics
    </div>
    """,
    unsafe_allow_html=True
)
