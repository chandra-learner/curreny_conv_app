import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json

with Image.open('curr_xchange.jpg') as image:
  st.image(image, width = 100, channels = 'RGB')

st.title('_Currency Converter App_')

#st.text("This app interconverts the value of foreign currencies!")
st.text("")
st.text("")


currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

base_curr = st.sidebar.selectbox('Select source currency', currency_list)
target_curr = st.sidebar.selectbox('Select target currency', currency_list)
qty = st.sidebar.text_input('Input Quantity', 1)
dt=st.sidebar.text_input('Exchange date in YYYY-MM-DD format', '2022-12-01')
qunatity = float(qty)

url = ''.join(["https://api.apilayer.com/exchangerates_data/convert?to=",target_curr,"&from=", base_curr, "&amount=","1","&date=",dt])

payload = {}
headers= {
  "apikey": "I5m1r5NCBm2UgsSTN9oslv2R1N2KU02o"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
df = pd.DataFrame(result)
df_xchng = df['info']['rate'].astype(str)
tgt_amt = float(df_xchng) * qunatity


col1, col2, col3 = st.columns(3)
col1.metric(base_curr, qunatity, )
col2.metric(target_curr, tgt_amt, )
col3.metric("EXCHANGE DATE", dt)