import streamlit as st
import random

# 저녁 메뉴 리스트
menu_list = [
    "치킨",
    "피자",
    "햄버거",
    "떡볶이",
    "삼겹살",
    "초밥",
    "파스타",
    "김치찌개",
    "돈까스",
    "마라탕"
]

# 제목
st.title("🍽 오늘 저녁 추천 앱")

st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해줘요!")

# 버튼
if st.button("추천 받기"):
    menu = random.choice(menu_list)
    st.success(f"오늘 저녁은 👉 {menu}")
