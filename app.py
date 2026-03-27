import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

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

X = df[['Age','Weight','Height','Goal']]
y = df[['Calories','Protein']]

model = LinearRegression()
model.fit(X,y)

st.title("🍽 Smart Nutrition AI")

age = st.number_input("Age", 10, 80)
weight = st.number_input("Weight (kg)", 30, 120)
height = st.number_input("Height (cm)", 100, 220)

goal = st.selectbox("Goal", ["Weight Loss","Maintain","Weight Gain"])
goal_map = {"Weight Loss":0,"Maintain":1,"Weight Gain":2}

if st.button("Get Diet Plan"):
    input_data = pd.DataFrame([[age,weight,height,goal_map[goal]]],
                             columns=['Age','Weight','Height','Goal'])

    prediction = model.predict(input_data)

    calories = round(prediction[0][0],2)
    protein = round(prediction[0][1],2)

    if calories < 1800:
        food = "Fruits, Salads, Oats"
    elif calories < 2300:
        food = "Rice, Dal, Vegetables, Chicken"
    else:
        food = "Eggs, Paneer, Nuts"

    st.success(f"🔥 Calories: {calories}")
    st.success(f"💪 Protein: {protein}")
    st.info(f"🥗 {food}")
