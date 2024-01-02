import pickle
import numpy as np
import streamlit as st
from keras.models import load_model
model = load_model('svm1.sav')
st.title('Prediksi Kenaikan Permukaan Air Laut Terhadap Banjir')                         

TinggiLaut = st.text_input('Ketinggian Laut')      
KecepatanAngin = st.text_input('Kecepatan Angin')    
GangguanCuaca = st.text_input('Gangguan Cuaca')      
Astronomi = st.text_input('Astronomi')   
with open('requirements.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()
prediksibanjir = ''
   
if st.button('Prediksi Kenaikan Permukaan Laut Terhadap Banjir'):
    prediksibanjir = model.predict([[TinggiLaut, KecepatanAngin, GangguanCuaca, Astronomi]])
    if prediksibanjir[0] == 1:
        prediksibanjir = 'Terprediksi Kenaikan Permukaan Laut berpotensi Banjir'
    else:
        prediksibanjir = 'Tidak Terprediksi Kenaikan Permukaan Laut berpotensi Banjir'

    st.success(prediksibanjir)

