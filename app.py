from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

# Optional: Create logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Dummy prediction logic (replace with real model later)
        predicted_price = round((data['present_price'] * 0.7 - data['owner'] * 0.5 + data['year'] * 0.001), 2)

        # Save prediction to a file with UTF-8 encoding
        with open('logs/predictions.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | Input: {data} | Predicted Price: ₹{predicted_price}\n")

        return jsonify({"predicted_price": predicted_price})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        fb = request.get_json()

        # Save feedback with UTF-8 encoding
        with open('logs/feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | Feedback: {fb['feedback']}\n")

        return jsonify({"message": "Feedback submitted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
