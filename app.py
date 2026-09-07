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
# NATIVE STREAMLIT FLOW CARD
# =========================================================

def display_flow_card(trade):

    direction = str(trade["direction"])
    score = int(trade["score"])

    confidence = get_confidence(score)

    if direction == "CALL":
        direction_icon = "🟢"
        direction_color = "#62d69d"
        border_color = "#58d69b"
        card_bg = "#173d30"
        signal_type = "BULLISH"
    else:
        direction_icon = "🔴"
        direction_color = "#ff737d"
        border_color = "#ff5964"
        card_bg = "#4b282d"
        signal_type = "BEARISH"

    # Card container
    with st.container(border=True):

        # HEADER
        col_title, col_confidence = st.columns([3, 1])

        with col_title:

            st.markdown(
                f"""
                <div style="
                    font-size:28px;
                    font-weight:800;
                    color:#f4f5f7;
                    padding-top:5px;
                ">
                    {direction_icon} {trade["ticker"]} —
                    <span style="color:{direction_color};">
                        {direction}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption("BUYING DETECTED")

        with col_confidence:

            st.markdown(
                f"""
                <div style="
                    background:{card_bg};
                    border:1px solid {border_color};
                    color:{direction_color};
                    padding:10px;
                    border-radius:10px;
                    text-align:center;
                    font-weight:700;
                    margin-top:8px;
                ">
                    {confidence}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        # ROW 1
        col1, col2, col3 = st.columns(3)

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

        # ROW 2
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Contracts",
                f"{int(trade['contracts']):,}"
            )

        with col2:
            st.metric(
                "Strike",
                f"${float(trade['strike']):,.0f}"
            )

        with col3:
            st.metric(
                "Premium",
                f"${float(trade['premium']):,.0f}"
            )

        # ROW 3
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Volume vs Average",
                f"{float(trade['volume_ratio']):.1f}x"
            )

        with col2:
            st.metric(
                "Unusual Volume",
                trade["unusual_volume"]
            )

        with col3:
            sweep_value = (
                "⚡ YES"
                if trade["sweep"] == "YES"
                else "NO"
            )

            st.metric(
                "Sweep Detected",
                sweep_value
            )

        # ROW 4
        col1, col2, col3 = st.columns(3)

        with col1:
            block_value = (
                "🧱 YES"
                if trade["block_trade"] == "YES"
                else "NO"
            )

            st.metric(
                "Block Trade",
                block_value
            )

        with col2:
            st.metric(
                "Transaction",
                trade["transaction"]
            )

        with col3:
            st.metric(
                "Signal Type",
                signal_type
            )

        st.divider()

        # FINAL SIGNAL
        st.markdown(
            f"""
            <div style="
                font-size:18px;
                font-weight:700;
                padding:12px;
                border-radius:8px;
                background:{card_bg};
                border-left:4px solid {border_color};
                color:#f1f3f7;
            ">
                Institutional Smart Money Signal:
                <span style="color:{direction_color};">
                    {trade["signal"]}
                </span>
            </div>
            """,
            unsafe_allow_html=True
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
