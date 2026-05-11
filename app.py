import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction App", page_icon="🩺")

st.title("🩺 Diabetes Prediction")
st.write("Nhập các thông số y tế để dự đoán bệnh tiểu đường.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, value=2)
glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
blood_pressure = st.number_input("BloodPressure", min_value=0.0, value=70.0)
skin_thickness = st.number_input("SkinThickness", min_value=0.0, value=20.0)
insulin = st.number_input("Insulin", min_value=0.0, value=80.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0, value=0.5)
age = st.number_input("Age", min_value=1, value=30)

if st.button("Predict"):
    data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()

        prediction = result["prediction"]

        if prediction == 1:
            st.error("⚠️ Kết quả: Có khả năng bị tiểu đường (1)")
        else:
            st.success("✅ Kết quả: Không bị tiểu đường (0)")

    except Exception as e:
        st.error(f"Lỗi kết nối API: {e}")