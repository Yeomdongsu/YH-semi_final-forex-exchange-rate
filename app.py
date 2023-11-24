import streamlit as st
from app_home import app_run_home
from app_eda import app_run_eda
from app_diff import app_run_diff 

def main() :
    menu = ["프로젝트 소개","EDA (Exploratory Data Analysis)","다양한 통화의 환율을 비교 해보기"]
    selectbox = st.sidebar.selectbox("Menu", menu)

    if selectbox == menu[0] :
        app_run_home()
    elif selectbox == menu[1] :
        app_run_eda()
    elif selectbox == menu[2] :
        app_run_diff()        

if __name__ == "__main__" : main()