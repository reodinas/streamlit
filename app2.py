import streamlit as st


def main():
    st.title('웹 대시보드')
    
    print('웹 대시보드')

    st.text('웹 대시보드 개발하기')

    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 서브헤더 영역')

    st.success('성공했을 때 메시지를 보여줄 때 사용')
    st.warning('경고 메세지를 보여주고 싶을 때')
    st.info('정보성 메세지를 보여주고 싶을 때')
    st.error('문제가 발생했음을 보여주고 싶을 때')

    # 파이썬의 함수들의 설명을 보여주고 싶을 때
    st.help(sum)
    st.help(len)

if __name__ == '__main__':
    main()