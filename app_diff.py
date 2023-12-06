import streamlit as st
import pandas as pd
from datetime import datetime
from pytube import YouTube

def app_run_diff() :
    st.info("다양한 통화의 환율을 비교하여 상대 가치 식별하는 페이지 입니다.")
    st.markdown("\n")
    st.markdown("\n")
    
    df = pd.read_csv("./data/daily_forex_rates.csv")

    index_name = df[df.columns[2]].value_counts().index

    select_date = st.date_input("원하는 날짜를 고르세요")
    
    select_date = select_date.strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%Y-%m-%d")

    if select_date > now_time : 
        st.error("아직 다가오지 않은 날짜를 선택하지 마세요")
    else :
        st.success(f"{select_date}가 입력되었습니다.")    
    st.markdown("\n")

    select_country = st.multiselect("두 나라 선택", index_name, placeholder="대소문자 구분 없이 영어로 입력하세요.", max_selections=2)
    
    if len(select_country) == 2 :
        st.success(f"{select_country[0]} , {select_country[1]}가 입력되었습니다.")
    elif len(select_country) == 1 :
        st.warning("나라 하나를 더 선택하세요.")
    else : 
        st.text("")

    st.markdown("\n")

    if st.checkbox("비교하기") :

        if len(select_country) != 2 :
            st.error("올바르게 선택해주세요.")
        else :
            country_1 = df.loc[(df[df.columns[2]] == select_country[0]) & (df[df.columns[-1]] == select_date)]
            country_2 = df.loc[(df[df.columns[2]] == select_country[1]) & (df[df.columns[-1]] == select_date)]

            if country_1.empty or country_2.empty :
                st.warning("해당 날짜에 데이터가 없습니다.")     
            else :
                country_1 = country_1[df.columns[-2]].values[0] # 1335.1
                country_2 = country_2[df.columns[-2]].values[0] 

                split_country_1 = select_country[0].split() # Won
                split_country_name_1 = " ".join(split_country_1[:-1]) # South Korean
                split_country_2 = select_country[1].split()
                split_country_name_2 = " ".join(split_country_2[:-1])
                
        
                st.info(f"{select_date}일의 1유로당 가격은 \n\n{split_country_name_1}에서는 {round(country_1 , 3)} {split_country_1[-1]} 이고 {split_country_name_2}에서는 {round(country_2 , 3)} {split_country_2[-1]} 입니다.")

                in_num = st.number_input(f"{split_country_name_1}의 금액을 적어주세요.", min_value=0, max_value=100000000, placeholder="숫자만 입력하세요.")
                st.markdown("\n")
                if in_num != 0 : 

                    con_1 = int(country_1 / country_1) # 무조건 1.0
                    con_2 = round(country_2 / country_1 , 3) # 소수점 셋째자리까지만 나오게 

                    in_num_res = in_num * con_1 # 사용자가 입력한 값
                    in_num_res2 = round(in_num * con_2 , 4) 

                    st.info(f"{split_country_name_1}의 1 {split_country_1[-1]}은(는) {split_country_name_2}의 {con_2} {split_country_2[-1]}와 같습니다. \n\n{split_country_2[-1]} 은(는) 소수점 셋째 자리까지만 나오게 했습니다. \n\n 그러므로 약간의 오차가 있을 수 있습니다.")
                    st.markdown("\n")
                    st.success(f"{split_country_name_1}의 {in_num_res} {split_country_1[-1]}은(는) {split_country_name_2}의 {in_num_res2} {split_country_2[-1]}와 같습니다.")

    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # st.markdown("\n")
    # if st.checkbox("클릭") :
    #     yt = YouTube("https://youtu.be/-GsrYvZoAdA") 
    #     video_stream = yt.streams.get_highest_resolution()
    #     youtube = video_stream.url

    #     st.video(youtube)               