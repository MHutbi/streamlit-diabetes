import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('prediksi diabetes')

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Pragnancies')

with col2 :
    Glucose = st.text_input ('input nilai Glucose')

with col1 :
    BloodPressure = st.text_input ('input nilai BloodPressure')

with col2 :
    SkinThickness = st.text_input ('input nilai SkinThickness')

with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai DiabetesPedigreeFunction')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol prediksi
if st.button('test prediksi diabetes') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 0) :
        diab_diagnosis = 'pasien terkena diabetes'

    else :
        diab_diagnosis = 'pasien tidak terkena diabetes'
    st.success(diab_diagnosis)
        

