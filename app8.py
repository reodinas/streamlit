import streamlit as st

# 다른 파일의 함수를 호출하고 싶으면, 함수를 임포트 한다.
from app8_home import run_home_app
from app8_EDA import run_eda_app
from app8_ML import run_ml_app
from app8_about import run_about_app

def main():
    st.title('파일 분리 앱')
    
    # EDA : Exploratory Data Analysis 탐색적 데이터 분석
    menu = ['Home', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home_app()

    elif choice == 'EDA':
        run_eda_app()

    elif choice == 'ML':
        run_ml_app()

    elif choice == 'About':
        run_about_app





if __name__ == '__main__':
    main()