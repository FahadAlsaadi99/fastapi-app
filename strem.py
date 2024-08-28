import streamlit as st
import requests

st.title("Car Price Prediction")


year = st.number_input("Year", min_value=1980, max_value=2024, value=2020)
engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=7.0, value=2.5)
mileage = st.number_input("Mileage", min_value=0.0, max_value=500000.0, value=15000.0)
car_type = st.selectbox("Type", ["Accent", "Land Cruiser"])
make = st.selectbox("Make", ["Hyundai", "Mercedes"])
options = st.selectbox("Options", ["Full", "Standard"])


if st.button("Predict"):
    response = requests.post(f"https://fastapi-app-5xa4.onrender.com/predict", json={
        "Year": year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Type": car_type,
        "Make": make,
        "Options": options
    })
    
    if response.status_code == 200:
        prediction = response.json().get("pred")
        st.write(f"The predicted cluster is: {prediction}")
    else:
        st.write("Error: Could not get prediction from the API")

