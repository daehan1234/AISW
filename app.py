import streamlit as st
import random

# 음식 리스트
food_list = ['피자', '햄버거', '스시', '파스타', '라면', '샌드위치', '초밥', '떡볶이', '치킨', '부대찌개']

# 제목과 설명
st.title("랜덤 음식 추천기")
st.write("오늘 뭐 먹을지 고민되나요? 버튼을 눌러 랜덤 음식을 추천받아보세요!")

# 버튼이 눌리면 랜덤 음식 추천
if st.button("음식 추천 받기"):
    recommended_food = random.choice(food_list)
    st.success(f"오늘의 추천 음식!!!!!!!!1: {recommended_food}")

# 음식 목록을 보여주는 기능 추가
if st.checkbox("DD 목록 보기"):

    st.write(food_list)
