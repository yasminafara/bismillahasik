import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm
import joblib

# Load the dataset
databanjir = pd.read_csv('hasilsmote.csv')

# Load the SVM model
classifier = svm.SVC(kernel='linear')
X = databanjir.drop(columns='rob', axis=1)
Y = databanjir['rob']
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
classifier.fit(X, Y)

# Save the SVM model as a .sav file
joblib.dump(classifier, 'svm_model.sav')

# Streamlit UI
st.title("Potential Flooding Prediction App")

st.sidebar.header("User Input")
st.sidebar.markdown(
    "Enter the environmental factors to predict potential flooding.")

# User input
tinggi_laut = st.sidebar.slider(
    "Sea Level", min_value=1.0, max_value=2.0, step=0.1, value=1.5)
kecepatan_angin = st.sidebar.slider(
    "Wind Speed", min_value=0, max_value=25, value=15)
gangguan_cuaca = st.sidebar.selectbox("Weather Disturbance", [0, 1])
gelombang = st.sidebar.slider(
    "Wave Height", min_value=0.5, max_value=2.0, step=0.25, value=1.0)
astronomi = st.sidebar.selectbox("Astronomical Factors", [0, 1])

# Make prediction
input_data = np.array([tinggi_laut, kecepatan_angin,
                      gangguan_cuaca, gelombang, astronomi]).reshape(1, -1)
std_data = scaler.transform(input_data)
prediction = classifier.predict(std_data)

# Display prediction
st.subheader("Prediction:")
if prediction[0] == 0:
    st.success('Tidak berpotensi naiknya air laut dan banjir')
    st.text("Potential Flooding Value: 0")
else:
    st.error('Berpotensi naiknya air laut menyebabkan banjir')
    st.text("Potential Flooding Value: 1")

# Display the dataset
st.subheader("Potensi:")
st.dataframe(std_data)

# Display the dataset
st.subheader("Dataset:")
st.dataframe(databanjir)

# Display some statistics
st.subheader("Statistics:")
st.write(databanjir.describe())

# Display correlation heatmap
st.subheader("Correlation Heatmap:")
st.image('correlation_heatmap.png',
         caption='Correlation Heatmap', use_column_width=True)
