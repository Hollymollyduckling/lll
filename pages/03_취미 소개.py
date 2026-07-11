import streamlit as st

st.set_page_config(page_title="취미 소개", page_icon="🎨")

st.title("🎨 내가 좋아하는 취미들")
st.write(" 주말이나 여가 시간에 주로 하는 활동들입니다.")

hobby = st.selectbox("어떤 취미를 보시겠어요?", ["📸 사진 촬영", "🏃‍♂️ 러닝 & 운동", "☕ 예쁜 카페 탐방"])

if hobby == "📸 사진 촬영":
    st.subheader("찰나의 순간을 기록하기")
    st.write("풍경이나 사람들의 자연스러운 모습을 카메라에 담을 때 큰 행복을 느낍니다.")
    st.image("https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500", width=400)
    
elif hobby == "🏃‍♂️ 러닝 & 운동":
    st.subheader("땀 흘리며 스트레스 해소하기")
    st.write("주 3회 한강을 달리며 체력을 기르고 복잡한 생각을 정리하곤 합니다.")
    st.image("https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=500", width=400)
    
elif hobby == "☕ 예쁜 카페 탐방":
    st.subheader("커피 향과 함께하는 여유")
    st.write("잔잔한 음악이 흐르는 카페에서 책을 읽거나 노트북으로 작업하는 것을 좋아합니다.")
    st.image("https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=500", width=400)
