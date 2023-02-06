import streamlit as st
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
#from xgboost import XGBRegressor
import numpy as np
import re
import datetime
import pickle
st.header("Rossmann Sales Prediction App")

store_new_df = pd.read_csv(r"store_new_feat.csv")

# load best model [vishnu] not loading the model as some problem in loading best model in this github repository, no issues in local
#best_xgboost_model = xgb.XGBRegressor()
#best_xgboost_model.load_model("rassmann_best_model.json")

Store = ""
Store = st.text_input("Store: Enter the Store Number (1 to 1115): ")
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
Promo = st.text_input("Promo: Enter a value(0 or 1)")
Promo2 = st.text_input("Promo2: Enter a value (0 or 1)")
PerCentDiseaseAffInWeek = st.text_input("PerCentDiseaseAffInWeek: Enter expected % of Disease in that week (0 to 100)")
PromoInterval = st.selectbox('PromoIntreval: Select one value from list', (['nan', 'Jan,Apr,Jul,Oct', 'Feb,May,Aug,Nov', 'Mar,Jun,Sept,Dec']))
if Store != "":
    StoreType = store_new_df.loc[store_new_df.Store == Store, 'StoreType'].values[0]
    Assortment = store_new_df.loc[store_new_df.Store == Store, 'Assortment'].values[0]
    AvgSalesPerStore = store_new_df.loc[store_new_df.Store == Store, 'AvgSalesPerStore'].values[0]
    AvgCustomersPerStore = store_new_df.loc[store_new_df.Store == Store, 'AvgCustomersPerStore'].values[0]
    MedSalesPerStore = store_new_df.loc[store_new_df.Store == Store, 'MedSalesPerStore'].values[0]
    MedCustomersPerStore = store_new_df.loc[store_new_df.Store == Store, 'MedCustomersPerStore'].values[0]
    AvgCustSpentInStore = store_new_df.loc[store_new_df.Store == Store, 'AvgCustSpentInStore'].values[0]
    #LastWeekSalesPerStore = store_new_df.loc[store_new_df.Store == Store, 'LastWeekSalesPerStore'].values[0]
    LastWeekCustomersPerStore = store_new_df.loc[store_new_df.Store == Store, 'LastWeekCustomersPerStore'].values[0]

Query_data = []
Features = [Store,DayOfWeek,Promo,StateHoliday,SchoolHoliday,StoreType,Assortment,CompetitionDistance,CompetitionOpenSinceMonth,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek,Promo2SinceYear,PromoInterval,Year,Month,Week,PerCentDiseaseAffInWeek,AvgSalesPerStore,AvgCustomersPerStore,MedSalesPerStore,MedCustomersPerStore,AvgCustSpentInStore,LastWeekCustomersPerStore]
#LastWeekSalesPerStore
for ele in Features:
    Query_data.append(ele)
st.write(Query_data)
Query_data = np.array(Query_data)
Query_data = Query_data[np.newaxis,:]


if st.button('Make Sales Prediction'):
    prediction = 6325
    #[vishnu] not loaded the model as some problem in loading best model in this github repository, no issues in local, so hard coding as discussed
    #best_xgboost_model.predict(Query_data)
    st.write("Sales Prediction for the Store is: "+str(prediction[-1]))
