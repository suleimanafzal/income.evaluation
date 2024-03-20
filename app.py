#!/usr/bin/env python3.11.5

from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the saved models
models = {}
for name in ['KNN', 'SVM', 'Naive Bayes', 'Logistic Regression', 'Decision Tree']:
    models[name] = load(f'{name}_model.joblib')

# Define endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data
    data = request.json

    # Make predictions using each model
    predictions = {}
    for name, model in models.items():
        predictions[name] = model.predict([data['features']])[0]

    # Return predictions
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)