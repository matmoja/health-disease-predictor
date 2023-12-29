import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes_prediction():
    form_data = request.form if request.method == 'POST' else {}
    
    result = additional_info = None

    if request.method == 'POST':
        # Retrieve input data from the form
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bloodPressure = float(request.form['bloodPressure'])
        skinThickness = float(request.form['skinThickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetesPedigreeFunction = float(request.form['diabetesPedigreeFunction'])
        age = float(request.form['age'])
        
    
           

        # Code for prediction
        diab_prediction = diabetes_model.predict([[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]])

        result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        
        
        # Additional information or comparisons to the norm can be added here
        additional_info = 'Additional information goes here'
        

        return render_template('diabetes.html', result=result, additional_info = additional_info, form_data=form_data)

    return render_template('diabetes.html', form_data=form_data)

@app.route('/heart_disease', methods=['GET', 'POST'])
def heart_disease_prediction():
    form_data = request.form if request.method == 'POST' else {}
    
    result = additional_info = None

    if request.method == 'POST':
        # Retrieve input data from the form
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])
      

        # Code for prediction
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        
        # Additional information or comparisons to the norm can be added here
        additional_info = 'Additional information goes here'

        return render_template('heart_disease.html', result=result, additional_info = additional_info, form_data=form_data)

    return render_template('heart_disease.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
