import streamlit as st

# 전체 페이지 기본 설정 (타이틀, 아이콘, 레이아웃)
st.set_page_config(
    page_title="나를 소개하는 공간",
    page_icon="🏡",
    layout="centered"
)

# 홈 화면 콘텐츠
st.title("👋 안녕하세요! 저를 소개합니다")
st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800", caption="Welcome to my profile website!")

st.markdown("""
### ✨ 이 사이트에 오신 것을 환영합니다!
이곳은 저의 성격, 직업, 취미, 이상형, 그리고 장점까지 저라는 사람을 다각도로 소개해 드리는 개인 포트폴리오 공간입니다.

**왼쪽 사이드바의 메뉴**를 클릭하여 저에 대해 더 자세히 알아보세요!👇
""")

st.divider()
st.info("💡 팁: 사이드바가 보이지 않는다면 왼쪽 상단의 `>` 버튼을 눌러보세요.")
