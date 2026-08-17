from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import io
import os

# Initialize Flask app
superkart_api = Flask(__name__)

# Define the directory where models are saved
# Since superkart_api.py is inside backend_files, we look in the current directory
MODEL_DIR = '.'

# Load the preprocessor and model
try:
    preprocessor = joblib.load(os.path.join(MODEL_DIR, 'preprocessor.joblib'))
    model = joblib.load(os.path.join(MODEL_DIR, 'superkart_model.joblib'))
    print("Preprocessor and model loaded successfully.")
except Exception as e:
    print(f"Error loading model or preprocessor: {e}")
    preprocessor = None
    model = None

# Helper function to preprocess input and make prediction
def make_prediction(input_df):
    if preprocessor is None or model is None:
        return {"error": "Model or preprocessor not loaded."}

    try:
        # Transform input data using the preprocessor
        processed_input = preprocessor.transform(input_df)

        # Make prediction
        prediction = model.predict(processed_input)
        return prediction.tolist()
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}


# Online inference endpoint
@superkart_api.route('/v1/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Convert single JSON object to DataFrame
    input_df = pd.DataFrame([data])

    predictions = make_prediction(input_df)

    if "error" in predictions:
        return jsonify(predictions), 500

    return jsonify({"prediction": predictions[0]})

# Batch inference endpoint
@superkart_api.route('/v1/predictbatch', methods=['POST'])
def predict_batch():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            # Read CSV data into a DataFrame
            csv_data = io.StringIO(file.stream.read().decode("UTF8"))
            input_df = pd.read_csv(csv_data)

            predictions = make_prediction(input_df)

            if "error" in predictions:
                return jsonify(predictions), 500

            # Return predictions as a dictionary mapping index to prediction
            return jsonify({str(i): pred for i, pred in enumerate(predictions)})
        except Exception as e:
            return jsonify({"error": f"Failed to process CSV file or make predictions: {e}"}), 500
    else:
        return jsonify({"error": "Invalid file type. Please upload a CSV file."}), 400

# Health check endpoint
@superkart_api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # In a production/containerized environment, host='0.0.0.0' is necessary
    superkart_api.run(host='0.0.0.0', port=5000)
