import streamlit as st
import pandas as pd
import numpy as np

def create_random_dataframe():
    return pd.DataFrame(
        np.random.randn(2, 3), 
        columns=['A', 'B', 'C']
    )

st.title('Task 2: 데이터 표시하기')

st.subheader('데이터프레임')

df = create_random_dataframe()
st.dataframe(df)
