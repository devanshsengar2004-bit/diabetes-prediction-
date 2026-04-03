# Diabetes Prediction System 

A Machine Learning-based web application that predicts whether a person is diabetic or not based on medical input values.

## Live Demo
Run locally using the steps below.

## Tech Stack
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Model:** Random Forest Classifier
- **Frontend:** HTML, CSS
- **Dataset:** Pima Indians Diabetes Dataset (Kaggle)

## Features
- Predicts diabetes risk based on 5 medical inputs
- 77% model accuracy on 154 test patients
- Clean and responsive web interface
- Real-time prediction without page reload

##  Dataset
- 768 patients records
- 8 features: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age
- Target: 0 = Not Diabetic, 1 = Diabetic

## How to Run
1. Clone the repository
   git clone https://github.com/devanshsengar2004-bit/diabetes-prediction-.git

2. Install dependencies
   pip install flask scikit-learn pandas numpy

3. Run the application
   python app.py

4. Open in browser
   http://127.0.0.1:5000

## Project Structure
- app.py — Flask backend and ML model
- diabetes.py — Model training and evaluation
- templates/index.html — Frontend form
- static/style.css — Styling
- diabetes.csv — Dataset

## Developer
Devansh Singh Sengar
MCA Student — IILM University, Greater Noida
