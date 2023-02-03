import streamlit as st
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
#from xgboost import XGBRegressor
import numpy as np
import re
import datetime
st.header("Rossmann Sales Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/gurokeretcha/WishWeightPredictionApplication/master/Fish.csv")
#load label encoder
#encoder = LabelEncoder()
#encoder.classes_ = np.load('classes.npy',allow_pickle=True)

# load model
best_xgboost_model = xgb.XGBRegressor()
#best_xgboost_model.load_model("best_model.json")

if st.checkbox('Show Training Dataframe'):
    data



Store = st.text_input("Store: Enter the Store Number (1 to 1115): ");
date1 = st.date_input("Date: Enter date, on Sales forecast needed:")
Day =  date1.day
Year =  date1.year
Promo2SinceYear =  date1.year
CompetitionOpenSinceYear = date1.year
Month = date1.month
CompetitionOpenSinceMonth = date1.month
Week = datetime.date(Year, Month, Day).isocalendar().week
Promo2SinceWeek = datetime.date(Year, Month, Day).isocalendar().week
#1 to 7 (Europe Week start day and end day, Mon and Sun) based on Date.
DayOfWeek = datetime.date(Year, Month, Day).isoweekday()
StateHoliday = st.text_input("StateHoliday: If above selected Date is, enter a for public holiday, b for Easter holiday, c for Christmas, 0 for None")
SchoolHoliday = st.text_input("SchoolHoliday: On above selected Date Sales will be affected, Enter 1 for yes, 0 for No")
CompetitionDistance = st.text_input("CompetitionDistance: How far away (meters) competitor from the Store "+str(Store))
Promo = st.text_input("Promo: Enter a value(0 or 1) ")
Promo2 = st.text_input("Promo2: Enter a value (0 or 1) ")
PromoInterval = st.selectbox('PromoIntreval: Select one value from list', (['nan', 'Jan,Apr,Jul,Oct', 'Feb,May,Aug,Nov', 'Mar,Jun,Sept,Dec']))
Query_data = []
Features = [Store,DayOfWeek,Promo,StateHoliday,SchoolHoliday]
#,StoreType,Assortment,CompetitionDistance,CompetitionOpenSinceMonth,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek,Promo2SinceYear,PromoInterval,Year,Month,Week,PerCentDiseaseAffInWeek,AvgSalesPerStore,AvgCustomersPerStore,MedSalesPerStore,MedCustomersPerStore,AvgCustSpentInStore,LastWeekSalesPerStore,LastWeekCustomersPerStore]
for ele in Features:
    Query_data.append(ele)
st.write(Query_data)


"""if st.button('Make Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), input_Length1, input_Length2, input_Length3, input_Height, input_Width], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your fish weight is: {np.squeeze(prediction, -1):.2f}g")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.write(f"If you want to see more advanced applications you can follow me on [medium](https://medium.com/@gkeretchashvili)")"""
