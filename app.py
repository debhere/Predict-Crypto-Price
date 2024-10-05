import streamlit as st
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
    selection = f'You have selected {crypto} for {pred_dt} {pred_tm}'
    st.write(selection)