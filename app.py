import pandas as pd
import pickle as pk
import streamlit as st

model= pk.load(open(r'C:\Users\HP\Downloads\Lets se\model1_pkl','rb'))
st.header("Delhi Houses Price Prediction")
df = pd.read_csv(r"C:\Users\HP\Downloads\Lets se\Cleaned_data.csv")


area =st.number_input("Enter Area Required")
bed =st.number_input("Enter No Of Bedrooms")
bath =st.number_input("Enter No Of Bathrooms")
fur =st.text_input("Furnish Required")

input = pd.DataFrame([[area , bed , bath , fur ]],columns=["area",	"bedrooms" ,"bathrooms" , "furnishingstatus"])

if st.button("Predict Price"):
    output=model.predict(input)
    out_str = "Price Of the House is"+ str(output[0]*100000)

