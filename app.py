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
        return "⚪ NEUTRAL FLOW"
    else:
        return "🔵 LOW CONVICTION"


# =========================================================
# FLOW CARD DISPLAY FUNCTION
# =========================================================

def display_flow_card(trade):

    direction = str(trade["direction"])
    score = int(trade["score"])

    if direction == "CALL":
        direction_icon = "🟢"
        direction_color = "#62d69d"
        signal_type = "BULLISH"
    else:
        direction_icon = "🔴"
        direction_color = "#ff737d"
        signal_type = "BEARISH"

    confidence = get_confidence(score)

    # Card Header
    st.markdown(
        f"""
<div style="
background-color:#222d3d;
border-radius:15px;
padding:25px;
margin-bottom:10px;
border-left:6px solid {direction_color};
">

<div style="
font-size:28px;
font-weight:800;
color:#f4f5f7;
margin-bottom:10px;
">
{direction_icon} {trade["ticker"]} —
<span style="color:{direction_color};">{direction}</span>
</div>

<div style="
font-size:16px;
color:#aeb7c5;
margin-bottom:20px;
">
BUYING DETECTED • {confidence}
</div>
</div>
""",
        unsafe_allow_html=True
    )

    # Metrics Row 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Institutional Activity",
            trade["activity"]
        )

    with col2:
        st.metric(
            "Institutional Score",
            f"{score}/100"
        )

    with col3:
        st.metric(
            "Expiration",
            trade["expiration"]
        )

    with col4:
        st.metric(
            "Contracts",
            f"{int(trade['contracts']):,}"
        )

    # Metrics Row 2
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Strike",
            f"${float(trade['strike']):,.0f}"
        )

    with col2:
        st.metric(
            "Premium",
            f"${float(trade['premium']):,.0f}"
        )

    with col3:
        st.metric(
            "Volume vs Average",
            f"{float(trade['volume_ratio']):.1f}x"
        )

    with col4:
        st.metric(
            "Unusual Volume",
            str(trade["unusual_volume"])
        )

    # Metrics Row 3
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Sweep Detected",
            str(trade["sweep"])
        )

    with col2:
        st.metric(
            "Block Trade",
            str(trade["block_trade"])
        )

    with col3:
        st.metric(
            "Transaction",
            str(trade["transaction"])
        )

    with col4:
        st.metric(
            "Signal",
            signal_type
        )

    st.info(
        f"🎯 Institutional Smart Money Signal: {trade['signal']}"
    )

    st.write("")


# =========================================================
# DISPLAY HIGHEST CONVICTION TRADE
# =========================================================

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


# =========================================================
# DISPLAY REMAINING TRADES
# =========================================================

remaining_trades = filtered_df.iloc[1:]

for _, trade in remaining_trades.iterrows():
    display_flow_card(trade)
