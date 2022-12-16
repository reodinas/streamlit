import streamlit as st
import pandas as pd

# 웹페이지에서 차트를 그릴 때 깔끔한 plotly 라이브러리
import plotly.express as px
# altair 라이브러리
import altair as alt


def main():
    df = pd.read_csv('streamlit_data/lang_data.csv')

    st.dataframe(df.head())

    column_menu = df.columns[1:]

    choice_list = st.multiselect('프로그래밍 언어를 선택하세요.', column_menu)

    if len(choice_list) != 0:
        # 유저가 선택한 언어만, 차트를 그린다.
        df_selected = df[choice_list]

        # 스트림릿에서 제공하는 라인차트
        st.line_chart(df_selected)

        # 스트림릿에서 제공하는 영역차트
        st.area_chart(df_selected)

        # 스트림릿에서 제공하는 바차트
        st.bar_chart(df_selected)


    df3 = pd.read_csv('streamlit_data/iris.csv')
    
    ### altair 라이브러리의 mark_circle 함수 사용법
    chart = alt.Chart(df3).mark_circle().encode(
        x='petal_length',
        y='petal_width',
        color = 'species'
    )
    st.altair_chart(chart)

    ### 위치 정보를 지도에 표시하는 방법
    ### 스트림릿의 map 차트
    df2 = pd.read_csv('streamlit_data/location.csv', index_col=0)
    st.dataframe(df2.head(3))

    st.map(df2, zoom=10)


    df4 = pd.read_csv('streamlit_data/prog_languages_data.csv', index_col=0)
    st.dataframe(df4.head())

    ### plotly의 pie차트 그리는 방법
    fig = px.pie(df4, 'lang', 'Sum', title='각 언어별 파이차트')
    st.plotly_chart(fig)

    ### plotly의 bar 차트 그리는 방법
    fig2 = px.bar(df4, x='lang', y='Sum')
    st.plotly_chart(fig2)
    ### 내림차순 정렬
    df_sorted = df4.sort_values('Sum', ascending=False)
    fig3 = px.bar(df_sorted, x='lang', y='Sum')
    st.plotly_chart(fig3)


if __name__ == '__main__':
    main()