import streamlit as st # type: ignore
import pandas as pd

from prophet.serialize import model_from_json # type: ignore

import time
from datetime import datetime

d = datetime.now()
t = d.time()

st.title("Cypto Price Prediction")

# content = """
# This is a simple app to predict the price of a crypto currency. 
# Currently, the app is only capable of predicting Bitcoin prices. However, down the line
# we will add other crypto assets as well. Stay tuned!

# """

# def stream_content():
#     for word in content.split(" "):
#         yield word + " "
#         time.sleep(0.2) 


# st.write_stream(stream_content) 

#crypto, pred_dt, pred_tm = None, None, None

col1, col2, col3 = st.columns(3)

with col1:
    crypto = col1.selectbox("Select currency of your choice",
                        ("Bitcoin"))
with col2:
    pred_dt = col2.date_input("Select your date", d)

with col3:
    pred_tm = col3.time_input("select your time", value="now", step=60)



btnLabel = f"Predict {crypto} prices"

if st.button(btnLabel):
    #selection = f'You have selected {crypto} for {pred_dt} {pred_tm}'
    
    pred_dt = str(pred_dt)
    pred_tm = str(pred_tm)   
    dt_str = pred_dt +" "+ pred_tm

    ds = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    cols = {
        'ds': [ds]
    }
    df = pd.DataFrame(cols)

    with open('serialized_model.json', 'r') as fin:
        model = model_from_json(fin.read())
        f = model.predict(df)
        prediction = f['yhat'].values[0]
        
        prediction_text = f"The predicted {crypto} price for {ds} is {prediction}"
    
    st.write(prediction_text)