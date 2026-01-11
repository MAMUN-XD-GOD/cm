from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from core.core_brain import analyze_trade
from core.learning_engine import feedback

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No screenshot uploaded"}), 400

    pair = request.form.get("pair", "XAU/USD")
    timeframe = request.form.get("timeframe", "1m")

    image = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    result = analyze_trade(image_path, pair, timeframe)
    return jsonify(result)

@app.route("/feedback", methods=["POST"])
def send_feedback():
    data = request.json
    result = data.get("result")
    signal = data.get("signal")
    pair = data.get("pair")
    timeframe = data.get("timeframe")

    stats = feedback(result, signal, pair, timeframe)
    return jsonify({"status": "ok", "stats": stats})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
