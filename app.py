from flask import Flask, request, jsonify, send_from_directory
from core.image_loader import load_image
from core.market_detector import detect_market
from core.candle_reader import read_candles
from core.structure import analyze_structure
from core.signal_engine import generate_signal
from core.expiry_engine import suggest_expiry
from core.risk_guard import risk_check
from utils.confidence_score import confidence_score

app = Flask(__name__)

@app.route("/")
def ui():
    return send_from_directory("ui", "index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img = load_image(request.files["image"])
    if img is None:
        return jsonify({"error": "Invalid or unclear screenshot"}), 400

    market = detect_market(img)
    candles = read_candles(img)
    structure = analyze_structure(candles)

    risk = risk_check(candles, structure)
    if not risk["allow"]:
        return jsonify({
            "signal": "WAIT",
            "reason": risk["reason"]
        })

    signal = generate_signal(candles, structure)
    expiry = suggest_expiry(candles)
    confidence = confidence_score(candles, structure)

    return jsonify({
        "market": market,
        "signal": signal,
        "expiry": expiry,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
