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
        highlight_class = "call-highlight"
        confidence_class = "confidence-call"
        score_class = "score-call"
        value_class = "call-value"

        direction_html = '<span class="call-highlight">CALL</span>'
        signal_icon = "🟢"

    else:

        card_class = "flow-card put-card"
        highlight_class = "put-highlight"
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
            {signal_icon} {ticker} — {direction_html}<br>
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

    return textwrap.dedent(card_html).strip()
