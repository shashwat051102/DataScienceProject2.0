from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
import pandas as pd
import joblib
from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.Prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# Load the trained model
model_path = "artifacts/model_trainer/model.joblib"
model = None

def load_model():
    """Load the trained model"""
    global model
    try:
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            logger.info("Model loaded successfully")
        else:
            logger.error(f"Model file not found at {model_path}")
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")

@app.route('/', methods=["GET"])  ## Route to display the home page
def index():
    """Render the main prediction form"""
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Load model if not already loaded
        if model is None:
            load_model()
        
        if model is None:
            return render_template('index.html', error="Model not available. Please train the model first.")
        
        # Extract form data
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]
        
        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        # Round to 2 decimal places
        prediction = round(prediction, 2)
        
        # Prepare input data for display
        inputs = {
            'fixed_acidity': request.form['fixed_acidity'],
            'volatile_acidity': request.form['volatile_acidity'],
            'citric_acid': request.form['citric_acid'],
            'residual_sugar': request.form['residual_sugar'],
            'chlorides': request.form['chlorides'],
            'free_sulfur_dioxide': request.form['free_sulfur_dioxide'],
            'total_sulfur_dioxide': request.form['total_sulfur_dioxide'],
            'density': request.form['density'],
            'pH': request.form['pH'],
            'sulphates': request.form['sulphates'],
            'alcohol': request.form['alcohol']
        }
        
        logger.info(f"Prediction made: {prediction} for inputs: {inputs}")
        
        # Render results page
        return render_template('results.html', prediction=prediction, inputs=inputs)
        
    except ValueError as e:
        logger.error(f"Invalid input data: {str(e)}")
        return render_template('index.html', error="Please enter valid numeric values for all fields.")
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return render_template('index.html', error="An error occurred during prediction. Please try again.")

@app.route('/results')
def results():
    """Direct access to results page - redirect to home"""
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('index.html', error="Page not found. Redirected to home."), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(e)}")
    return render_template('index.html', error="Internal server error. Please try again."), 500

if __name__ == '__main__':
    # Load model on startup
    load_model()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)