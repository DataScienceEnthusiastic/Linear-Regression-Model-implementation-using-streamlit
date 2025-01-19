import pandas as pd
import numpy as np
import pickle as pk 
import streamlit as st 

# import os
# model_path = os.path.join(os.getcwd(), 'Car', 'model.pkl')
# model = pk.load(open('model.pkl', 'rb'))


model = pk.load(open('model.pkl', 'rb'))

st.header('Car Price Predictor')

cars_data = pd.read_csv('Cardetails.csv')

#Getting the brand name 
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
cars_data['name']= cars_data['name'].apply(get_brand_name)


################Getting all data from user#########################
name = st.selectbox('Enter the brand name ',cars_data['name'].unique())
year = st.slider('Enter the year of manufactor',1994,2025)
km_driven = st.slider('Number of Km driven',11,200000)
fuel = st.selectbox('Enter the fuel type of car ',cars_data['fuel'].unique())
seller_type = st.selectbox('seller type',cars_data['seller_type'].unique())
transmission = st.selectbox('Enter the transmission ',cars_data['transmission'].unique())
owner = st.selectbox('Owner type',cars_data['owner'].unique())
mileage = st.slider('Mileage of car',1,30)
engine = st.slider('Engine CC',800,5000)
max_power = st.slider('Max power',0,200)
seats = st.slider('Number of seats',1,10)

############fedding the user data to the model##########################

if st.button('Predict the price of the car '):
    #Making an dataframe for predicting me own car's value , actaul value 6,61,000
    input_data_model = pd.DataFrame([[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]], columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
    

owner_dict = {
    'First Owner':1 ,'Second Owner':2, 'Third Owner':3,'Fourth & Above Owner':4,'Test Drive Car':5
}

#Or
input_data_model['owner'].replace(owner_dict, inplace=True)


seller_type_dict = {
    'Individual':1 ,'Dealer':2, 'Trustmark Dealer':3
}

#Or
input_data_model['seller_type'].replace(seller_type_dict, inplace=True)



fuel_dict = {
    'Diesel':1, 'Petrol':2, 'LPG':3, 'CNG':4
}

#Or
input_data_model['fuel'].replace(fuel_dict, inplace=True)


transmission_dict = {
    'Manual':1,'Automatic':2
}

#Or
input_data_model['transmission'].replace(transmission_dict, inplace=True)



import pandas as pd

replacement_dict = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5,
    'Ford': 6, 'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10,
    'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13, 'Mitsubishi': 14,
    'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'Lexus': 19,
    'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23, 'Daewoo': 24,
    'Kia': 25, 'Fiat': 26, 'Force': 27, 'Ambassador': 28, 'Ashok': 29,
    'Isuzu': 30, 'Opel': 31
}

# Correct and efficient replacement
#cars_data['name'] = cars_data['name'].map(replacement_dict)

#Or
input_data_model['name'].replace(replacement_dict, inplace=True)





#st.write(input_data_model)

car_price = model.predict(input_data_model)

st.markdown('Car price as per prediction is going to be : '+ str(car_price[0]))