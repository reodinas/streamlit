# 웹 대시보드에 이미지파일, 동영상파일 넣는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    # 이미지
    img = Image.open('streamlit_data/image_03.jpg')
    print(img)

    st.image(img)
    st.image(img, use_column_width=True) # 브라우저의 가로사이즈에 맞게

    image_url = 'https://www.ibric.org/upload/board/files/spcont/spc_9/0008719_1.jpg'
    st.image(image_url)


    # 동영상
    video_file = open('streamlit_data/secret_of_success.mp4', mode='rb') # rb: read binary
    st.video(video_file)

if __name__ == '__main__':
    main()