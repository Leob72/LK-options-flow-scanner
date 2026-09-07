# =========================================================
# FLOW CARD FUNCTION - CORREGIDA
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

    sweep_icon = "⚡" if str(trade["sweep"]) == "YES" else ""
    block_icon = "🧱" if str(trade["block_trade"]) == "YES" else ""

    card_html = (
        f'<div class="{card_class}">'
        
        f'<div class="flow-card-header">'
        
        f'<div class="flow-title">'
        f'{signal_icon} {ticker} — {direction_html}'
        f'<br>'
        f'<span style="font-size:15px; color:#aeb7c5;">BUYING DETECTED</span>'
        f'</div>'
        
        f'<span class="{confidence_class}">{confidence}</span>'
        
        f'</div>'

        f'<div class="info-grid">'

        f'<div class="info-box">'
        f'<div class="info-label">Institutional Activity</div>'
        f'<div class="info-value {value_class}">{activity}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Institutional Score</div>'
        f'<div class="info-value {score_class}">{score}/100</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Expiration</div>'
        f'<div class="info-value">{expiration}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Contracts</div>'
        f'<div class="info-value">{contracts:,} {direction}S</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Strike</div>'
        f'<div class="info-value">${strike:,.0f}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Premium</div>'
        f'<div class="info-value gold-value">${premium:,.0f}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Volume vs Average</div>'
        f'<div class="info-value gold-value">{volume_ratio:.1f}x</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Unusual Volume</div>'
        f'<div class="info-value gold-value">{unusual_volume}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Sweep Detected</div>'
        f'<div class="info-value">{sweep_icon} {html.escape(str(trade["sweep"]))}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Block Trade</div>'
        f'<div class="info-value">{block_icon} {html.escape(str(trade["block_trade"]))}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Transaction</div>'
        f'<div class="info-value {value_class}">{transaction}</div>'
        f'</div>'

        f'<div class="info-box">'
        f'<div class="info-label">Signal</div>'
        f'<div class="info-value {value_class}">{signal_icon} {signal}</div>'
        f'</div>'

        f'</div>'

        f'<div class="signal-box">'
        f'Institutional Smart Money Signal: '
        f'<span class="{value_class}">{signal}</span>'
        f'</div>'

        f'</div>'
    )

    return card_html
