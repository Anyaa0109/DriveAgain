from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime
import joblib
import numpy as np

app = Flask(__name__)

# Create logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Load the trained Linear Regression model
model = joblib.load('linear_reg_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html exists

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features in the same order as the model was trained
        features = np.array([[
            data['year'],
            data['present_price'],
            data['kms_driven'],
            data['fuel_type'],       # Already encoded: Petrol=0, Diesel=1, CNG=2
            data['seller_type'],     # Dealer=0, Individual=1
            data['transmission'],    # Manual=0, Automatic=1
            data['owner']
        ]])

        # Make prediction
        predicted_price = model.predict(features)[0]
        predicted_price = round(predicted_price, 2)

        # Log the prediction
        with open('logs/predictions.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | Input: {data} | Predicted Price: ₹{predicted_price}\n")

        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        fb = request.get_json()

        with open('logs/feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} | Feedback: {fb['feedback']}\n")

        return jsonify({"message": "Feedback submitted successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # For Render or local
    app.run(host="0.0.0.0", port=port)
