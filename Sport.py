import streamlit as st
import pandas as pd

# CSV 데이터 로드
data = pd.read_csv('exercise_data.csv')

st.title("맞춤 운동 추천 프로그램")

# 사용자 입력 받기
level = st.selectbox('운동 난이도를 선택하세요', data['난이도'].unique())
category = st.selectbox('운동 유형을 선택하세요', data['운동유형'].unique())

# 조건에 맞는 운동 추천
filtered_data = data[(data['난이도'] == level) & (data['운동유형'] == category)]

if not filtered_data.empty:
    for _, row in filtered_data.iterrows():
        st.write(f"**{row['운동명']}**: {row['추천시간']} 동안 수행하세요.")
else:
    st.write("해당 조건에 맞는 운동이 없습니다.")
