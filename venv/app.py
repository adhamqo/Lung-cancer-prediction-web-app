from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')

# Load the KNN model from the pickle file
with open('knn1.pkl', 'rb') as file:
    knn_model = pickle.load(file)

# Render the index HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Render the form HTML template
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Capture features from form (ensure these names match your HTML form input names)
        features = [
            int(request.form['age']),
            int(request.form['gender']),
            int(request.form['air_pollution']),
            int(request.form['alcohol_use']),
            int(request.form['dust_allergy']),
            int(request.form['occupational_hazards']),
            int(request.form['genetic_risk']),
            int(request.form['chronic_lung_disease']),
            int(request.form['balanced_diet']),
            int(request.form['obesity']),
            int(request.form['smoking']),
            int(request.form['passive_smoker']),
            int(request.form['chest_pain']),
            int(request.form['coughing_of_blood']),
            int(request.form['fatigue']),
            int(request.form['weight_loss']),
            int(request.form['shortness_of_breath']),
            int(request.form['wheezing']),
            int(request.form['swallowing_difficulty']),
            int(request.form['clubbing_of_finger_nails']),
            int(request.form['frequent_colds']),
            int(request.form['dry_cough']),
            int(request.form['snoring'])
        ]

        final_features = [np.array(features)]
        prediction = knn_model.predict(final_features)
        output = prediction[0]
        
        level_mapping = {0: 'Low', 1: 'Medium', 2: 'High'}
        prediction_text = f'Predicted Lung Cancer Severity Level: {level_mapping[output]}'
        
        return render_template('result.html', prediction_text=prediction_text)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('result.html', prediction_text=error_message)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port= 5000)