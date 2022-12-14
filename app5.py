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

    image_url = 'https://cdn.pixabay.com/photo/2022/11/19/18/45/gray-geese-7602847__340.jpg'
    st.image(image_url)


    # 비디오
    video_file = open('streamlit_data/secret_of_success.mp4', mode='rb') # rb: read binary
    st.video(video_file)


    # 오디오
    audio_file = open('streamlit_data/song.mp3', 'rb')
    st.audio(audio_file)


if __name__ == '__main__':
    main()

    