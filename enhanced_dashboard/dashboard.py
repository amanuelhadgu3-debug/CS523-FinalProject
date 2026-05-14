
import streamlit as st
import pandas as pd
import random

st.title("Real-Time Crypto Analytics Dashboard")

data = {
    "Coin": ["BTC", "ETH", "SOL", "XRP"],
    "Volume": [random.randint(100,1000) for _ in range(4)],
    "Price": [random.randint(100,60000) for _ in range(4)]
}

df = pd.DataFrame(data)

st.dataframe(df)
st.bar_chart(df.set_index("Coin")["Volume"])
