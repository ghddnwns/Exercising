app.py

import streamlit as st

# 애플리케이션 제목
st.title("맞춤형 운동 추천 프로그램")

# 사용자 입력
ability = st.selectbox("운동 능력 선택:", ["초급", "중급", "고급"])
time = st.selectbox("운동 시간대 선택:", ["아침", "오후", "저녁"])

# 운동 추천 로직
if ability == "초급":
    pushups, pullups, squats = 10, 5, 15
elif ability == "중급":
    pushups, pullups, squats = 20, 10, 30
else:
    pushups, pullups, squats = 30, 15, 45

# 추천 결과 출력
st.write(f"추천 운동: 팔굽혀펴기 {pushups}회, 턱걸이 {pullups}회, 스쿼트 {squats}회")

# 사용자가 운동 완료 여부 체크
completed = st.checkbox("오늘의 운동 완료!")

if completed:
    st.success("잘하셨습니다! 계속해서 도전하세요.")
