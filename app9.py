import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 차트를 웹브라우저에 보여주기

def main():
    st.title('차트 그리기 1')

    df = pd.read_csv('streamlit_data/iris.csv')

    st.dataframe(df.head())

    # sepal_length 와 sepal_width의 관계를 차트로 그리시오.
    fig = plt.figure()
    plt.scatter(data= df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)

    # 스트림릿에서 차트에 한글 나오게 설정하는 방법
    # https://luvris2.tistory.com/119

    # 히스토그램
    # petal_length 로 히스토그램 그리기
    fig3 = plt.figure()
    plt.hist(data=df, x='petal_length', bins=10, rwidth=0.8)
    st.pyplot(fig3)

    fig4 = plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='petal_length', bins=10, rwidth=0.8)

    plt.subplot(1, 2, 2)
    plt.hist(data=df, x='petal_length', bins=20, rwidth=0.8)
    st.pyplot(fig4)

    ''' 
    우리가 주피터노트북에서 그렸던
    plt차트나 sb차트는, 스트림릿에서 표시하려면
    plt.figure()로 먼저 영역을 잡아주고
    st.pyplor 함수로 웹 화면에 그려준다. 
        
    그리고 데이터 프레임의 내장 차트도, 마찬가지로 해준다
        
    df의 species 컬럼의 각 종별로 몇개의 데이터가 있는지 차트로
    '''

    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)

    fig6 = plt.figure()
    df['petal_length'].hist()
    st.pyplot(fig6)




if __name__ == '__main__':
    main()