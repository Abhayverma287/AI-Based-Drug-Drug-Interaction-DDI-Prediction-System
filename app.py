import streamlit as st
from src.predict import predict_interaction

st.title("AI Drug-Drug Interaction Predictor")

drug1 = st.text_input("Enter Drug 1")
drug2 = st.text_input("Enter Drug 2")

if st.button("Predict Interaction"):
    
    result = predict_interaction(drug1,drug2)
    
    st.success(result)