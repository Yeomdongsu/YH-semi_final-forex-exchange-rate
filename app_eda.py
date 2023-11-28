import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

def app_run_eda() :
    st.info("데이터를 분석하고 차트화 시키는 페이지 입니다.\n\n")

    df = pd.read_csv("./data/daily_forex_rates.csv")

    index_name = df[df.columns[2]].value_counts().index

    st.text_area("각 컬럼에 대한 설명",
                f"{df.columns[0]} : 국가별 통화 코드를 의미합니다. \n\n{df.columns[1]} : 기준 통화 코드를 의미합니다. 이 데이터에선 유로를 기준으로 합니다.\n\n{df.columns[2]} : 나라이름과 통화 이름을 의미합니다.\n\n{df.columns[3]} : 환율을 의미합니다.\n\n 날짜별 1유로당 해당 나라의 환율을 나타내는 데이터 입니다.", height=255)

    if st.checkbox("외환 환율 데이터 보기") :
        st.dataframe(df)

    st.markdown("\n")

    in_shape = df.shape
    in_n_count = dict(zip(df.isna().sum().index, df.isna().sum().values))
    in_country = df[df.columns[2]].nunique()
    in_date = df[df.columns[-1]].nunique()

    if st.checkbox("데이터 기본 정보 보기") :
        if st.button("전체 행과 열의 개수") :
            st.info(f"데이터 전체 행의 개수는 {in_shape[0]}개 , 열의 개수는 {in_shape[1]}개 입니다.")
        if st.button("NaN 여부") :
            st.write("컬럼명 : NaN 개수")
            for i,j in in_n_count.items() :
                st.write(f"{i} : {j}")
            st.info("전체 데이터의 NaN 개수는 0개 입니다.")        
        if st.button("총 나라의 개수") :        
            st.info(f"총 나라의 개수는 {in_country}개 입니다.")
        if st.button("날짜의 개수") :
            st.info(f"주말과 공휴일을 제외한 날짜의 개수는 {in_date}개 입니다.")    

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
        u_date_end = st.date_input("끝 날짜를 지정하세요.")

        _u_date_start = u_date_start.strftime("%Y년 %m월 %d일 %A")
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
                st.success(f"{_u_date_start} ~ {_u_date_end} 까지의 1유로당 외환 환율 데이터 입니다.")
                st.dataframe(u_total)

                uu = u_country.split()

                st.success(f"{_u_date_start} ~ {_u_date_end} 까지의 \n\n1유로당 몇 {uu[-1]}인지 알려주는 차트이며 차트당 6개월을 나타냅니다.")

                def plot_chart(start_idx , end_idx) :
                    fig = plt.figure(figsize=(12,6))
                    plt.plot(u_total["date"].iloc[start_idx : end_idx] ,u_total["exchange_rate"].iloc[start_idx : end_idx], color="green", linewidth=1.7)
                    plt.gca().xaxis.set_major_locator(months)
                    plt.gca().xaxis.set_major_formatter(monFmt)

                    plt.grid(True)
                    plt.title("Exchange_rate by Date")
                    plt.xlabel("Date")
                    plt.ylabel("Exchange_rate")
                    return fig

                n = len(u_total["date"]) 

                u_total["date"] = pd.to_datetime(u_total["date"]) # datetime 타입으로 변환
                months = MonthLocator() # 1달씩 나오게
                monFmt = DateFormatter('%Y-%m') # 표시 형식 포맷

                if n % 130 == 0 : 
                    count = n // 130 
                    
                    if count == 1 :
                        fig = plot_chart(0, n)
                        st.pyplot(fig)
                    else :
                        for i in range(count) : 
                            start_idx = i * 130
                            end_idx = (i+1) * 130
                            fig = plot_chart(start_idx, end_idx)
                            st.pyplot(fig)
                else :
                    count = (n // 130) + 1
                        
                    if count == 1 : 
                        fig = plot_chart(0, n)
                        st.pyplot(fig)
                    else :
                        for i in range(count-1) : 
                            start_idx = i * 130
                            end_idx = (i+1) * 130
                            fig = plot_chart(start_idx, end_idx)
                            st.pyplot(fig)
                
                        start_idx = (count-1) * 130
                        end_idx = n
                        fig = plot_chart(start_idx, n)
                        st.pyplot(fig)
    
    st.markdown("\n")
    
    mm_country = st.selectbox("2004년부터 어제까지 외환 환율의 최소값과 최대값, 그에 해당하는 날짜를 알고싶은 currency_name을 골라주세요", index_name)  

    cname = mm_country.split() # cname[-1] = Won
    cname_join = " ".join(cname[:-1]) # cname_join = "South Korean"

    ex_min = df[df[df.columns[2]] == mm_country].nsmallest(1, df.columns[3]).iloc[0,-2]
    ex_min_date = df[df[df.columns[2]] == mm_country].nsmallest(1, df.columns[3]).iloc[0,-1]

    ex_min_date = datetime.strptime(ex_min_date, "%Y-%m-%d").date()
    ex_min_date = ex_min_date.strftime("%Y년 %m월 %d일 %A")

    ex_max = df[df[df.columns[2]] == mm_country].nlargest(1, df.columns[3]).iloc[0,-2]
    ex_max_date = df[df[df.columns[2]] == mm_country].nlargest(1, df.columns[3]).iloc[0,-1]

    ex_max_date = datetime.strptime(ex_max_date, "%Y-%m-%d").date()
    ex_max_date = ex_max_date.strftime("%Y년 %m월 %d일 %A")

    st.info(f"{cname_join}는(은)\n\n {ex_min_date}에 외환 환율 최소값 {ex_min} {cname[-1]}였고,\n\n{ex_max_date}에 최대값 {ex_max} {cname[-1]}였습니다.")

            
            