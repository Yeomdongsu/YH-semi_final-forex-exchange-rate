import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sb
import altair as alt

def app_run_eda() :
    st.subheader("EDA 페이지")

    st.info("데이터를 분석하고 차트화 시키는 페이지 입니다.\n\n")

    df = pd.read_csv("./data/daily_forex_rates.csv")

    index_name = df[df.columns[2]].value_counts().index

    st.text_area("각 컬럼에 대한 설명",
                f"{df.columns[0]} : 국가별 통화 코드를 의미합니다. \n\n{df.columns[1]} : 기준 통화 코드를 의미합니다. 전부 유로를 기준으로 합니다.\n\n{df.columns[2]} : 통화 이름을 의미합니다.\n\n{df.columns[3]} : 환율을 의미합니다.\n\n 날짜별 1유로당 해당 나라의 환율을 나타내는 데이터 입니다.", height=255)

    if st.checkbox("외환 환율 데이터 보기") :
        st.dataframe(df)

    st.markdown("\n")

    if st.checkbox("총 나라의 개수") :
        country = df["currency_name"].nunique()
        st.write(f"총 나라의 개수는 {country}개 입니다.")

    st.markdown("\n")

    if st.checkbox("모든 나라의 통화 코드와 화폐 이름") :
        array1 = df[df.columns[0]].unique()
        array2 = df[df.columns[2]].unique()
        currency_dict = dict(zip(array1, array2))

        st.write("통화코드 , 나라와 화폐명")

        for i,j in currency_dict.items() :
            st.write(f"{i} , {j}")

    st.markdown("\n")

    if st.checkbox("기간별 해당 나라의 환율 검색") : 

        u_country = st.selectbox("알고싶은 currency_name을 골라주세요", index_name)

        st.info(f"{u_country}이(가) 입력되었습니다.")
                
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

            u_total = df.loc[(df[df.columns[2]] == u_country) & (df[df.columns[-1]].values >= str(u_date_start)) 
                            & (df[df.columns[-1]].values <= str(u_date_end))]
                 
            u_total = u_total.sort_values(df.columns[-1])

            if u_total.empty :
                st.warning("해당 조건에 맞는 데이터가 없습니다.")
            else : 
                st.success(f"{_u_date_start} ~ {_u_date_end} 까지의 1유로당 외환 환율 입니다.")
                st.dataframe(u_total)

                # half_idx = len(u_total) // 2
                # u_total_part1 = u_total.iloc[:half_idx, :]
                # u_total_part2 = u_total.iloc[half_idx:, :]

                # # 차트를 나란히 표시하기 위해 컬럼을 생성
                # col1, col2 = st.columns(2)

                # # 첫 번째 차트
                # with col1:
                #     st.subheader('Part 1')
                #     chart_part1 = alt.Chart(u_total_part1).mark_line().encode(
                #         x='date:T',
                #         y='exchange_rate:Q',
                #         color='currency_name:N'
                #     ).properties(
                #         width=500,
                #         height=300
                #     )
                #     st.altair_chart(chart_part1)

                # # 두 번째 차트
                # with col2:
                #     st.subheader('Part 2')
                #     chart_part2 = alt.Chart(u_total_part2).mark_line().encode(
                #         x='date:T',
                #         y='exchange_rate:Q',
                #         color='currency_name:N'
                #     ).properties(
                #         width=500,
                #         height=300
                #     )
                #     st.altair_chart(chart_part2)

                fig = plt.figure()
                sb.lineplot(data=u_total, x='date', y='exchange_rate')
                st.pyplot(fig)
    
    st.markdown("\n")
    
    mm_country = st.selectbox("2004년부터 어제까지 외환 환율의 최소값과 최대값, 그에 해당하는 날짜를 알고싶은 currency_name을 골라주세요", index_name)  

    cname = mm_country.split()
    cname_join = " ".join(cname[:-1])

    ex_min = df.loc[df[df.columns[2]] == mm_country].min().values[3:][0]
    ex_min_date = df.loc[df[df.columns[2]] == mm_country].min().values[3:][1]

    ex_min_date = datetime.strptime(ex_min_date, "%Y-%m-%d").date()
    ex_min_date = ex_min_date.strftime("%Y년 %m월 %d일 %A")

    ex_max = df.loc[df[df.columns[2]] == mm_country].max().values[3:][0]
    ex_max_date = df.loc[df[df.columns[2]] == mm_country].max().values[3:][1]

    ex_max_date = datetime.strptime(ex_max_date, "%Y-%m-%d").date()
    ex_max_date = ex_max_date.strftime("%Y년 %m월 %d일 %A")

    st.success(f"{cname_join}는(은)\n\n {ex_min_date}에 외환 환율 최소값 {ex_min} {cname[-1]}였고,\n\n{ex_max_date}에 최대값 {ex_max} {cname[-1]}였습니다.")

            
            