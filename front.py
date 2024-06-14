import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")
c1,c2 = st.columns([0.5,0.5])

with c1:
# brand
  company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
  type_ = st.selectbox('Type',df['TypeName'].unique())

# Ram
  ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
  weight = st.number_input('Weight of the Laptop')

# Touchscreen
  touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
  ips = st.selectbox('IPS',['No','Yes'])

# screen size
  screen_size = st.number_input('Screen Size')

# resolution
  resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
  cpu = st.selectbox('CPU',df['Cpu_brand'].unique())

  hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

  ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

  gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

  os = st.selectbox('OS',df['os'].unique())

  cat = st.selectbox('category', df['CPU_Category'].unique())

  if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
   # Ensure the query is a 2D array
    query = np.array([[company, type_, ram, weight, touchscreen, ips, ppi, cpu, cat, hdd, ssd, gpu, os]])

# Convert the query to a DataFrame
    query_df = pd.DataFrame(query, columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'ips',
       'ppi', 'Cpu_brand', 'CPU_Category', 'HDD', 'SSD', 'Gpu_brand', 'os'])

# Use the pipeline to make a prediction
    predicted_price = pipe.predict(query_df)

# Display the predicted price
    st.title(f"The predicted price is {np.exp(predicted_price[0])}")

