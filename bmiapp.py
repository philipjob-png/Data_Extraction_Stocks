import streamlit as st

st.title("BMI Calculator")
st.write("Calculate BMI")
#Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
height = st.number_input("Enter your height (meters)", min_value=0.5, max_value=3.0, value=1.75, step=0.01)
#Calculate BMI when button clicked
if st.button("Calculate BMI"):
#BMI Formula: (weight/height)*height
bmi = (weight/height)*height
st.subheader(f"Your BMI: {bmi:.2f}")
