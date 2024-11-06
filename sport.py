import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="맞춤 운동 추천 프로그램",
    page_icon="💪",
    layout="wide"
)

# CSS 스타일 적용
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# 데이터 로드
@st.cache_data
def load_data():
    try:
        return pd.read_csv('exercise_data.csv')
    except FileNotFoundError:
        st.error("⚠️ 'exercise_data.csv' 파일을 찾을 수 없습니다.")
        st.stop()

def main():
    st.title("💪 맞춤 운동 추천 프로그램")
    
    # 데이터 로드
    data = load_data()
    
    # 사이드바에 사용자 정보 입력
    with st.sidebar:
        st.header("🎯 운동 목표 설정")
        
        # 사용자 기본 정보
        name = st.text_input("이름", "사용자")
        age = st.number_input("나이", 15, 100, 30)
        weight = st.number_input("체중(kg)", 30.0, 200.0, 70.0)
        
        # 운동 선호도
        st.subheader("운동 선호도 설정")
        level = st.select_slider(
            '운동 난이도',
            options=['초급', '중급', '고급'],
            value='초급'
        )
        
        preferred_time = st.slider(
            '선호하는 운동 시간(분)',
            15, 120, 30, step=15
        )

    # 메인 영역
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 운동 유형 선택")
        category = st.multiselect(
            '관심 있는 운동 유형을 선택하세요',
            data['운동유형'].unique(),
            default=[data['운동유형'].iloc[0]]
        )

    # 운동 추천
    filtered_data = data[
        (data['난이도'] == level) & 
        (data['운동유형'].isin(category))
    ]

    with col2:
        st.subheader("📊 맞춤 운동 프로그램")
        if not filtered_data.empty:
            for _, row in filtered_data.iterrows():
                with st.expander(f"🏃‍♂️ {row['운동명']}"):
                    st.markdown(f"""
                        - **난이도**: {row['난이도']}
                        - **추천 시간**: {row['추천시간']}
                        - **소모 칼로리**: {row['예상칼로리']}kcal
                        - **운동 부위**: {row['운동부위']}
                        - **준비물**: {row['준비물']}
                    """)
                    if row['주의사항']:
                        st.warning(f"⚠️ 주의사항: {row['주의사항']}")

    # 통계 및 시각화
    st.subheader("📈 운동 분석")
    if not filtered_data.empty:
        fig = px.bar(
            filtered_data,
            x='운동명',
            y='예상칼로리',
            title='운동별 예상 소모 칼로리',
            color='운동유형'
        )
        st.plotly_chart(fig)

        # 총 운동 시간과 예상 소모 칼로리 계산
        total_time = sum([int(time.split('분')[0]) for time in filtered_data['추천시간']])
        total_calories = filtered_data['예상칼로리'].sum()

        # 메트릭스 표시
        col1, col2 = st.columns(2)
        col1.metric("총 운동 시간", f"{total_time}분")
        col2.metric("총 예상 소모 칼로리", f"{total_calories}kcal")

    # 운동 일지
    st.subheader("📝 운동 일지")
    if st.button("오늘의 운동 완료!"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.success(f"🎉 {name}님, {now}에 운동을 완료하셨습니다!")
        st.balloons()

if __name__ == "__main__":
    main()
