import streamlit as st
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np
import re
import datetime
import pickle
st.header("Rossmann Sales Prediction App")

store_new_df = pd.read_csv(r"store_new_feat.csv")
if st.checkbox('Show Store New Features From Dataframe'):
    store_new_df

# load best model [vishnu] not loading the model as some problem in loading best model in this github repository, no issues in local
#best_xgboost_model = xgb.XGBRegressor()
#best_xgboost_model.load_model("rassmann_best_model.json")

Store = 112#st.text_input("Store: Enter the Store Number (1 to 1115): ")

