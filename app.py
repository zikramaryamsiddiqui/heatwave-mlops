from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load saved model files
model = joblib.load("model/heatwave_best_model.pkl")
scaler = joblib.load("model/heatwave_scaler.pkl")
feature_order = joblib.load("model/heatwave_feature_order.pkl")

app = Flask(__name__)


def predict_heatwave(data):
    # Convert JSON input to DataFrame
    input_data = pd.DataFrame([data])

    # Keep exactly the 23 features in the training order
    input_data = input_data.reindex(columns=feature_order)

    # Check for missing values
    if input_data.isnull().any().any():
        missing = input_data.columns[
            input_data.isnull().any()
        ].tolist()

        raise ValueError(
            f"Missing or invalid features: {missing}"
        )

    # Match training data type
    if "is_monsoon_season" in input_data.columns:
        input_data["is_monsoon_season"] = (
            input_data["is_monsoon_season"].astype(int)
        )

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0][1]

    return int(prediction), float(probability)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Heatwave Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        prediction, probability = predict_heatwave(data)

        return jsonify({
            "heatwave_prediction": prediction,
            "prediction_label": (
                "Heatwave"
                if prediction == 1
                else "No Heatwave"
            ),
            "heatwave_probability": probability
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=False
    )