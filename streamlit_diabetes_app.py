import streamlit as st
from app.predictor import predict_diabetes

st.set_page_config(page_title="Diabetes Predictor", layout="centered")

st.title("🩺 Diabetes Prediction System")
st.markdown("### Enter patient details below")

# Input form
Pregnancies = st.number_input("Pregnancies", 0, 20, 1)
Glucose = st.number_input("Glucose", 0, 200, 120)
BloodPressure = st.number_input("Blood Pressure", 0, 200, 70)
SkinThickness = st.number_input("Skin Thickness", 0, 100, 20)
Insulin = st.number_input("Insulin", 0, 900, 80)
BMI = st.number_input("BMI", 0.0, 70.0, 25.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
Age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    # label, prob, risk = predict_diabetes(input_data)

    # st.subheader("📊 Prediction Result")
    # st.write(f"**Prediction:** {label}")
    # st.write(f"**Probability:** {prob:.4f}")
    # st.write(f"**Risk Level:** {risk}")

    result = predict_diabetes(input_data)

    label = result["prediction"]
    prob = float(result["probability"])
    risk = result["risk"]
    
    st.subheader("📊 Prediction Result")
    st.write(f"**Prediction:** {label}")
    st.write(f"**Probability:** {prob:.4f}")
    st.write(f"**Risk Level:** {risk}")

    if prob > 0.5:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")