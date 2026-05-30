# 🎓 Student Performance Predictor

## 📌 Overview

The Student Performance Predictor is a Machine Learning-based web application that predicts a student's final academic performance based on various educational and behavioral factors.

The system analyzes student attributes such as attendance, study hours, previous grades, extracurricular participation, and parental support to estimate the expected final grade and provide personalized recommendations for improvement.

---

## 🚀 Live Demo

🔗 Streamlit App:

https://studentperformancereportml0liz.streamlit.app/

---

## 🎯 Problem Statement

Educational institutions often face challenges in identifying students who may require additional academic support. Traditional evaluation methods focus primarily on past examination results and often fail to leverage predictive analytics for future performance assessment.

This project aims to address this challenge by using Machine Learning techniques to:

* Predict student academic performance
* Identify key factors affecting outcomes
* Provide actionable recommendations
* Support data-driven educational decision making

---

## ✨ Features

### 📊 Performance Prediction

Predicts a student's final grade based on academic and behavioral factors.

### 💡 Personalized Recommendations

Provides suggestions to improve academic performance.

### 📈 Interactive Dashboard

Modern Streamlit dashboard with real-time predictions.

### 🎨 Dynamic User Interface

Includes animated backgrounds, performance indicators, and visual feedback.

### 📋 Student Summary

Displays all input parameters and prediction results in a structured format.

### 🤖 Machine Learning Powered

Uses Random Forest Regression for performance prediction.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Regressor

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Streamlit

### Deployment

* Streamlit Community Cloud

---

## 📂 Dataset

The dataset contains the following features:

| Feature                   | Description                   |
| ------------------------- | ----------------------------- |
| Gender                    | Student Gender                |
| AttendanceRate            | Attendance Percentage         |
| StudyHoursPerWeek         | Weekly Study Hours            |
| PreviousGrade             | Previous Academic Performance |
| ExtracurricularActivities | Participation Level           |
| ParentalSupport           | Level of Family Support       |
| FinalGrade                | Target Variable               |

The dataset was augmented using synthetic data generation techniques to increase training diversity and improve model learning.

Dataset Size:

* 1000 Student Records
* 9 Features

---

## 🧠 Machine Learning Workflow

### Data Collection

Student performance dataset creation and preprocessing.

### Data Preprocessing

* Label Encoding
* Feature Selection
* Data Cleaning

### Model Training

Random Forest Regressor was trained using the processed dataset.

### Evaluation Metrics

The model was evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Model Persistence

The trained model is saved using Pickle for deployment.

---

## 📊 Model Performance

| Metric   | Score |
| -------- | ----- |
| MAE      | 2.59  |
| RMSE     | 3.29  |
| R² Score | 0.79  |

The model explains approximately 79% of the variance in student performance, demonstrating strong predictive capability.
<img width="790" height="490" alt="image" src="https://github.com/user-attachments/assets/dd147453-b202-48c0-9afc-15a0fb965099" />


---

## 📸 Application Workflow

1. Enter student details.
2. Select attendance and study habits.
3. Provide academic information.
4. Click **Predict Performance**.
5. View predicted final grade.
6. Analyze recommendations.
7. Review performance category.

---

## 🖥️ Installation

Clone the repository:

```bash
git clone https://github.com/Monalisa2810/StudentPerformanceReportML.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
StudentPerformanceReportML/
│
├── student_performance_1000.csv
├── student_model.pkl
├── app.py
├── requirements.txt
├── SPR_ML.ipynb
└── README.md
```

---

## 🔮 Future Enhancements

* Deep Learning Models
* Multi-Student Comparison Dashboard
* Academic Risk Detection
* Attendance Analytics
* Performance Trend Analysis
* PDF Report Generation

---

## 👩‍💻 Author

Monalisa Das

B.Tech – Computer Science and Engineering

Machine Learning Project

---

## 📜 License

This project is developed for educational and academic purposes.
