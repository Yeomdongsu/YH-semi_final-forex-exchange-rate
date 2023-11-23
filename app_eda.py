import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def app_run_eda() :
    st.subheader("EDA 페이지")
    st.info("데이터를 분석하고 차트화 시키는 페이지 입니다.\n\n")

    df = pd.read_csv("./data/daily_forex_rates.csv")

    if st.checkbox("외환 환율 데이터 보기") :
        st.dataframe(df)
        st.write(f"각 컬럼에 대한 설명)\n\n"
                 f"{df.columns[0]} : 국가별 통화 코드를 의미합니다. ex) KRW -> 한국의 통화\n\n"
                  f"{df.columns[1]} : 기준 통화 코드를 의미합니다. 이 데이터에서는 전부 유료입니다.\n\n"
                  f"{df.columns[2]} : 통화 이름을 의미합니다. ex) South Korean Won -> 남한 원"
                  f"{df.columns[3]} : 환율을 의미합니다. ")
    
    

    