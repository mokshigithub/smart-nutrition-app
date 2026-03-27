import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Page settings
st.set_page_config(page_title="Smart Nutrition AI", layout="centered")

# Title
st.title("🍽 Smart Nutrition AI")
st.write("Get personalized diet recommendations using AI")

# Dataset
data = {
    "Age":[20,22,25,27,30,35],
    "Weight":[50,55,60,65,70,75],
    "Height":[160,165,170,172,175,178],
    "Goal":[0,0,1,1,2,2],
    "Calories":[1600,1700,2000,2100,2500,2700],
    "Protein":[60,65,80,85,110,120]
}

df = pd.DataFrame(data)

# Model training
X = df[['Age','Weight','Height','Goal']]
y = df[['Calories','Protein']]

model = LinearRegression()
model.fit(X,y)

# Inputs
age = st.number_input("Age", 10, 80)
weight = st.number_input("Weight (kg)", 30, 120)
height = st.number_input("Height (cm)", 100, 220)

goal = st.selectbox("Goal", ["Weight Loss","Maintain","Weight Gain"])
goal_map = {"Weight Loss":0,"Maintain":1,"Weight Gain":2}

# Button
if st.button("Get Diet Plan"):
    
    # Prediction
    input_data = pd.DataFrame([[age, weight, height, goal_map[goal]]],
                              columns=['Age','Weight','Height','Goal'])

    prediction = model.predict(input_data)

    calories = round(prediction[0][0],2)
    protein = round(prediction[0][1],2)

    # BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    # Food recommendation
    if goal_map[goal] == 0:
        food = "🥗 Weight Loss Diet: Oats, Fruits, Salads, Green Tea"
    elif goal_map[goal] == 1:
        food = "🍛 Balanced Diet: Rice, Dal, Vegetables, Chicken"
    else:
        food = "🍗 Weight Gain Diet: Eggs, Paneer, Nuts, Milk"

    # Output
    st.success(f"🔥 Calories Needed: {calories}")
    st.success(f"💪 Protein Needed: {protein}")
    st.info(f"📊 BMI: {round(bmi,2)} ({bmi_status})")
    st.info(food)

    # Health warning
    if bmi > 30:
        st.warning("⚠️ You may need medical consultation")
