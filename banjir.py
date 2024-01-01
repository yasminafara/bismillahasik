import pickle
import numpy as np
import streamlit as st

st.title('Prediksi Kenaikan Permukaan Air Laut Terhadap Banjir')                         

TinggiLaut = st.text_input('Ketinggian Laut')      
KecepatanAngin = st.text_input('Kecepatan Angin')    
GangguanCuaca = st.text_input('Gangguan Cuaca')      
Astronomi = st.text_input('Astronomi')   

 
