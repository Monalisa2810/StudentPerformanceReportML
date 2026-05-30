import streamlit as st
import pickle
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(
        -45deg,
        #0f172a,
        #1e293b,
        #312e81,
        #0f766e
    );
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.95);
}

/* Glass Cards */
.metric-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.15);
    text-align: center;
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 25px rgba(0,255,255,0.3);
}

/* Main Title */
.main-title {
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:#38bdf8;
}

/* Subtitle */
.subtitle {
    text-align:center;
    color:#e2e8f0;
    font-size:18px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    height:55px;
    width:100%;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #2563eb,
        #8b5cf6
    );
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius:15px;
    overflow:hidden;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class='main-title'>
🎓 AI Student Performance Predictor
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Predict academic performance using Machine Learning
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------

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

# --------------------------------------------------
# ENCODING
# --------------------------------------------------

gender_encoded = 1 if gender == "Male" else 0

parent_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}

parent_encoded = parent_map[parent_support]

# --------------------------------------------------
# DASHBOARD CARDS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='metric-card'>
        <h3>📅 Attendance</h3>
        <h1>{attendance}%</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='metric-card'>
        <h3>📚 Study Hours</h3>
        <h1>{study_hours}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='metric-card'>
        <h3>🎯 Previous Grade</h3>
        <h1>{previous_grade}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# PREDICT
# --------------------------------------------------

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

    st.subheader("📊 Prediction Results")

    st.metric(
        "Predicted Final Grade",
        prediction
    )

    st.progress(min(int(prediction), 100))

    # ---------------------------------------------
    # CATEGORY
    # ---------------------------------------------

    if prediction >= 90:

        st.balloons()

        st.markdown("""
        <div style="
            background:#16a34a;
            padding:20px;
            border-radius:15px;
            text-align:center;
            font-size:28px;
            font-weight:bold;">
            🌟 Excellent Performance
        </div>
        """, unsafe_allow_html=True)

    elif prediction >= 75:

        st.markdown("""
        <div style="
            background:#2563eb;
            padding:20px;
            border-radius:15px;
            text-align:center;
            font-size:28px;
            font-weight:bold;">
            ✅ Good Performance
        </div>
        """, unsafe_allow_html=True)

    elif prediction >= 60:

        st.markdown("""
        <div style="
            background:#ea580c;
            padding:20px;
            border-radius:15px;
            text-align:center;
            font-size:28px;
            font-weight:bold;">
            ⚠️ Average Performance
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
            background:#dc2626;
            padding:20px;
            border-radius:15px;
            text-align:center;
            font-size:28px;
            font-weight:bold;">
            ❌ Needs Improvement
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------

    st.subheader("💡 Personalized Recommendations")

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
            "Strengthen understanding of core subjects."
        )

    if extracurricular == 0:
        recommendations.append(
            "Participate in extracurricular activities."
        )

    if parent_support == "Low":
        recommendations.append(
            "Seek guidance from mentors or teachers."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent work! Maintain your current habits."
        )

    for rec in recommendations:
        st.success(rec)

    st.markdown("---")

    # ---------------------------------------------
    # SUMMARY TABLE
    # ---------------------------------------------

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

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Developed using Streamlit • Scikit-Learn • Random Forest Regression"
)