import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sb

def app_run_eda() :
    st.subheader("EDA 페이지")

    st.info("데이터를 분석하고 차트화 시키는 페이지 입니다.\n\n")

    df = pd.read_csv("./data/daily_forex_rates.csv")

    st.text_area("각 컬럼에 대한 설명", f"{df.columns[0]} : 국가별 통화 코드를 의미합니다. \n\n{df.columns[1]} : 기준 통화 코드를 의미합니다. 전부 유로를 기준으로 합니다.\n\n{df.columns[2]} : 통화 이름을 의미합니다.\n\n{df.columns[3]} : 환율을 의미합니다.\n\n날짜별 1유로당 해당 나라의 환율을 나타내는 데이터 입니다.", height=240)

    if st.checkbox("외환 환율 데이터 보기") :
        st.dataframe(df)
    st.markdown("\n")

    if st.checkbox("총 나라의 개수") :
        country = df["currency_name"].nunique()
        st.write(f"총 나라의 개수는 {country}개 입니다.")
    st.markdown("\n")

    if st.checkbox("각 나라와 그 나라의 화폐 이름") :
        country_name = df["currency_name"].unique()
        for i in country_name :
            st.write(i)
    st.markdown("\n")

    if st.checkbox("기간별 해당 나라의 환율 검색") : 
        u_country = st.text_input("궁금한 나라의 이름을 영어로 적고 enter를 쳐주세요.", placeholder="기억이 안난다면 아는 부분만 적어주세요.")
        
        if len(u_country) != 0 :
            condition_1 = df.loc[df[df.columns[2]].str.contains(u_country, case=False)]

            if not condition_1.empty :
                st.info(f"{u_country}이(가) 입력되었습니다.")
            else : 
                st.error("입력한 글자를 포함하는 나라가 없습니다.")
                u_country = ""
                
        u_date_start = st.date_input("시작 날짜를 지정하세요.")
        _u_date_start = u_date_start.strftime("%Y년 %m월 %d일 %A")

        u_date_end = st.date_input("끝 날짜를 지정하세요.")
        _u_date_end = u_date_end.strftime("%Y년 %m월 %d일 %A")

        if u_date_start > u_date_end :
            st.error("시작 날짜가 끝 날짜보다 클 수 없습니다.")

        elif u_date_start == u_date_end :
            st.info(f"{_u_date_start}가 입력 되었습니다.")

        else :    
            st.info(f"{_u_date_start} ~ {_u_date_end}가 입력 되었습니다.")
        
        if st.button("검색") :
            if u_country == "" : 
                st.error("나라 이름을 제대로 쳐주세요.")
            else :
                u_total = df.loc[(df[df.columns[2]].str.contains(u_country, case=False)) 
                                 & (df[df.columns[-1]].values >= str(u_date_start)) 
                                 & (df[df.columns[-1]].values <= str(u_date_end))]
                u_total = u_total.sort_values(df.columns[-1])

                if u_total.empty :
                    st.warning("해당 조건에 맞는 데이터가 없습니다.")
                else : 
                    st.success(f"{u_country} 또는 {u_country}가 포함된 나라의 {_u_date_start} ~ {_u_date_end}까지의 1유로당 환율입니다.")
                    st.dataframe(u_total)
            
            
            