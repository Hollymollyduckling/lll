import streamlit as st

st.set_page_config(page_title="이상형 소개", page_icon="💖")

st.title("💖 내가 꿈꾸는 이상형")
st.write("서로 긍정적인 영향을 주고받을 수 있는 사람을 좋아합니다.")

st.divider()

st.subheader("🌟 이런 사람에게 매력을 느껴요!")

col1, col2, col3 = st.columns(3)
col1.metric(label="1순위 가치관", value="대화가 잘 통하는 사람")
col2.metric(label="2순위 성향", value="다정하고 따뜻한 사람")
col3.metric(label="3순위 생활습관", value="자기계발을 즐기는 사람")

st.markdown("""
### 📝 조금 더 구체적으로 말하자면...
- **티키타카가 잘 되는 사람:** 사소한 이야기로도 함께 웃을 수 있는 유머 코드가 맞는 분이 좋아요.
- **감정 표현이 솔직한 사람:** 서운하거나 고마운 점을 쌓아두지 않고 예쁘게 말해주는 사람이 이상형입니다.
- **서로의 성장을 응원하는 사람:** 각자의 일이나 꿈을 존중하고, 함께 발전할 수 있는 성숙한 연애를 지향합니다.
""")
