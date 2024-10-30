import streamlit as st
import pandas as pd
import os

# 파일 로드 예외 처리
try:
    # 현재 디렉터리 확인 및 데이터 로드
    st.write(f"현재 디렉터리: {os.getcwd()}")
    st.write(f"파일 목록: {os.listdir()}")

    data = pd.read_csv('exercise_data.csv')
except FileNotFoundError:
    st.error("⚠️ 'exercise_data.csv' 파일을 찾을 수 없습니다. 파일 경로를 확인해 주세요.")
    st.stop()  # 파일이 없으면 앱을 중지합니다.

# 제목 출력
st.title("맞춤 운동 추천 프로그램")

# 사용자 입력 받기
level = st.selectbox('운동 난이도를 선택하세요', data['난이도'].unique())
category = st.selectbox('운동 유형을 선택하세요', data['운동유형'].unique())

# 조건에 맞는 운동 추천
filtered_data = data[(data['난이도'] == level) & (data['운동유형'] == category)]

if not filtered_data.empty:
    st.subheader("추천 운동 목록")
    for _, row in filtered_data.iterrows():
        st.write(f"**{row['운동명']}**: {row['추천시간']} 동안 수행하세요.")
else:
    st.warning("❗ 해당 조건에 맞는 운동이 없습니다.")

