import streamlit as st
import pickle
import pandas as pd

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------

with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------------------
# Title
# ---------------------------

st.title("🎓 Student Performance Predictor")
st.markdown(
    """
Predict student academic performance using Machine Learning.

This system analyzes:
- Attendance
- Study Hours
- Previous Grades
- Extracurricular Activities
- Parental Support
"""
)

st.divider()

# ---------------------------
# Sidebar Inputs
# ---------------------------

st.sidebar.header("📋 Student Information")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

attendance = st.sidebar.slider(
    "Attendance Rate (%)",
    60,
    100,
    85
)

study_hours = st.sidebar.slider(
    "Study Hours Per Week",
    5,
    35,
    15
)

previous_grade = st.sidebar.slider(
    "Previous Grade",
    50,
    100,
    75
)

extracurricular = st.sidebar.slider(
    "Extracurricular Activities",
    0,
    3,
    1
)

parent_support = st.sidebar.selectbox(
    "Parental Support",
    ["Low", "Medium", "High"]
)

# ---------------------------
# Encoding
# ---------------------------

gender_encoded = 1 if gender == "Male" else 0

parent_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}

parent_encoded = parent_map[parent_support]

# ---------------------------
# Dashboard Layout
# ---------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Attendance",
    f"{attendance}%"
)

col2.metric(
    "Study Hours",
    study_hours
)

col3.metric(
    "Previous Grade",
    previous_grade
)

st.divider()

# ---------------------------
# Prediction Button
# ---------------------------

if st.button("🚀 Predict Performance"):

    sample = [[
        gender_encoded,
        attendance,
        study_hours,
        previous_grade,
        extracurricular,
        parent_encoded
    ]]

    prediction = model.predict(sample)[0]

    prediction = round(prediction, 2)

    st.subheader("📊 Prediction Result")

    st.metric(
        "Predicted Final Grade",
        prediction
    )

    progress = min(int(prediction), 100)

    st.progress(progress)

    # -----------------------
    # Performance Category
    # -----------------------

    if prediction >= 90:
        category = "🌟 Excellent"
        color = "green"

    elif prediction >= 75:
        category = "✅ Good"

    elif prediction >= 60:
        category = "⚠️ Average"

    else:
        category = "❌ Needs Improvement"

    st.success(
        f"Performance Category: {category}"
    )

    # -----------------------
    # Recommendations
    # -----------------------

    st.subheader("💡 Recommendations")

    recommendations = []

    if attendance < 85:
        recommendations.append(
            "Increase attendance above 85%."
        )

    if study_hours < 15:
        recommendations.append(
            "Spend more time studying each week."
        )

    if previous_grade < 70:
        recommendations.append(
            "Focus on strengthening core concepts."
        )

    if extracurricular == 0:
        recommendations.append(
            "Participate in extracurricular activities."
        )

    if parent_support == "Low":
        recommendations.append(
            "Seek mentorship and academic guidance."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent work! Maintain your current performance."
        )

    for rec in recommendations:
        st.write("✔️", rec)

    # -----------------------
    # Student Summary
    # -----------------------

    st.subheader("📝 Student Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Gender",
            "Attendance",
            "Study Hours",
            "Previous Grade",
            "Extracurricular Activities",
            "Parental Support"
        ],
        "Value": [
            gender,
            attendance,
            study_hours,
            previous_grade,
            extracurricular,
            parent_support
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True
    )

st.divider()

st.caption(
    "Developed using Streamlit, Scikit-Learn and Random Forest Regression"
)