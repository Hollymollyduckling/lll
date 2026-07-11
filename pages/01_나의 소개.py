import streamlit as st

st.set_page_config(page_title="성격 소개", page_icon="👤")

st.title("👤 저의 성격을 소개합니다")
st.subheader("💡 키워드로 보는 나의 성격: #경청 #긍정적 #책임감")

# MBTI 레이아웃 예시
st.markdown("### 🔮 저의 MBTI는 **ENFP (또는 본인유형)** 입니다!")

col1, col2 = st.columns(2)
with col1:
    st.success("**E (외향형) & N (직관형)**")
    st.write("새로운 사람들과 대화하는 것을 즐기며, 늘 흥미롭고 창의적인 아이디어를 상상하는 것을 좋아합니다.")
with col2:
    st.success("**F (감정형) & P (인식형)**")
    st.write("주변 사람들의 감정에 깊게 공감하고 배려하며, 계획에 얽매이기보다 유연하고 자유로운 상황을 선호합니다.")

st.divider()
st.markdown("> \"타인의 이야기를 진심으로 듣고, 그 안에서 긍정적인 에너지를 이끌어내는 능력이 있습니다.\"")
