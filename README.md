# Lung Cancer Prediction Project

## Table of Contents

1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
    - [About the Dataset](#about-the-dataset)
    - [Dataset Source](#dataset-source)
    - [Columns](#columns)
3. [Pipeline Components](#pipeline-components)
    - [Data Preprocessing](#1-data-preprocessing)
    - [Feature Engineering](#2-feature-engineering)
    - [Model Training and Evaluation](#3-model-training-and-evaluation)
    - [Model Deployment](#4-model-deployment)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Deploying as Docker Image](#deploying-as-docker-image)
7. [Contribution Guidelines](#contribution-guidelines)
8. [License](#license)

## Project Overview

This project aims to predict the likelihood of a patient developing lung cancer based on various risk factors. The application features an end-to-end automated machine learning pipeline that includes data preprocessing, model training, evaluation, and deployment. This hands-on project emphasizes MLOps practices to automate ML workflows effectively.

## Dataset

### About the Dataset

This dataset contains information on patients with lung cancer, including their age, gender, air pollution exposure, alcohol use, dust allergy, occupational hazards, genetic risk, chronic lung disease, balanced diet, obesity, smoking status, passive smoker status, chest pain, coughing of blood, fatigue levels, weight loss, shortness of breath, wheezing, swallowing difficulty, clubbing of finger nails, frequent colds, dry coughs, and snoring.

### Dataset Source

The dataset is sourced from [Kaggle - Cancer Patients and Air Pollution: A New Link](https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link/data).

### Columns

- Age: The age of the patient 
- Gender: The gender of the patient
- Air Pollution: The level of air pollution exposure of the patient 
- Alcohol use: The level of alcohol use of the patient 
- Dust Allergy: The level of dust allergy of the patient 
- Occupational Hazards: The level of occupational hazards of the patient 
- Genetic Risk: The level of genetic risk of the patient
- Chronic Lung Disease: The level of chronic lung disease of the patient
- Balanced Diet: The level of balanced diet of the patient 
- Obesity: The level of obesity of the patient 
- Smoking: The level of smoking of the patient
- Passive Smoker: The level of passive smoker of the patient 
- Chest Pain: The level of chest pain of the patient
- Coughing of Blood: The level of coughing of blood of the patient 
- Fatigue: The level of fatigue of the patient
- Weight Loss: The level of weight loss of the patient 
- Shortness of Breath: The level of shortness of breath of the patient 
- Wheezing: The level of wheezing of the patient 
- Swallowing Difficulty: The level of swallowing difficulty of the patient 
- Clubbing of Finger Nails: The level of clubbing of finger nails of the patient 
- Frequent Colds: The level of frequent colds of the patient 
- Dry Coughs: The level of dry coughs of the patient 
- Snoring: The level of snoring of the patient 
- Level: The risk level of lung cancer 

## Pipeline Components

### 1. Data Preprocessing

Automated data cleaning and preprocessing scripts are used to prepare the dataset for training.

### 2. Feature Engineering

Automated feature extraction and selection are implemented to identify relevant features for the model.

### 3. Model Training and Evaluation

Multiple machine learning models are automatically trained and evaluated using appropriate metrics. The best-performing model is selected for deployment.

### 4. Model Deployment

A web application is developed using Flask to utilize the model for making predictions based on input data.

## Setup and Installation

To set up the environment and run the pipeline, follow these steps:

1. Clone the repository:

git clone <repository_url>
cd <repository_name>


2. Install the required packages:

pip install -r requirements.txt


3. Run the Flask application:

python app.py


4. Access the application at `http://localhost:5000` in your web browser.

## Usage

1. In the homepage, click on "Get Started" button to go to the form page.
2. Fill out the form with patient details.
3. After, filling the form click on the "Predict" button to see the predicted category of lung cancer risk.
4. Navigate to the result page to view the prediction.
5. There are two buttons to go back to the form page or go to the homepage. 

## Deploying as Docker Image

To deploy the Flask application as a Docker image, follow these steps:

1. Build the Docker image:

docker run -d -p 5000:5000 lung-cancer-prediction


3. Access the application at `http://localhost:5000` in your web browser.

## File Structure

lung-cancer-prediction/
│
├── Venv/
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ ├── static/
│ ├── templates/
│ │ ├── form.html
│ │ ├── index.html
│ │ └── result.html
│ ├── app.py
│ ├── dockerfile
│ ├── Knn1.pkl
│ ├── pyvenv.cfg
│ └── requirements.txt
│
├── README.md
└── LICENSE

## Contribution Guidelines

Contributions to the project are welcome! 

## License

(https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link/data)






