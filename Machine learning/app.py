import streamlit as st
import joblib
import numpy as np

# load model
#model = joblib.load('logistic_regression_model.pkl')
model = joblib.load(r'F:\AI_ML_classes\Machine learning\logistic_regression_model.pkl')

#scaler = joblib.load('scaler.pkl')
scaler = joblib.load(r'F:\AI_ML_classes\Machine learning\scaler.pkl')


st.title("Student Pass Prediction App")

# Input fields
study_hours = st.number_input("StudyHours")
attendence = st.number_input("Attendence")


## prediction button
if st.button("Predict"):
    input_data = np.array([[study_hours, attendence]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.success("Student will PASS!")
    else:
        st.error("Student will FAIL!")


 