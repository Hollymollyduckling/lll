import streamlit as st

st.set_page_config(page_title="직업 소개", page_icon="💼")

st.title("💼 저의 직업과 커리어를 소개합니다")

tab1, tab2 = st.tabs(["현재 하는 일", "비전 및 목표"])

with tab1:
    st.subheader("🚀 직무: 서비스 기획자 / 개발자 (예시)")
    st.write("현재 사용자의 불편함을 찾고 이를 기술로 해결하는 매력적인 직무에서 일하고 있습니다.")
    st.markdown("""
    **주요 업무 및 경험:**
    - 스트림릿을 활용한 프로토타입 웹 애플리케이션 구축
    - 데이터 기반의 사용자 경험(UX) 개선 프로젝트 리드
    - 다양한 팀원들과의 유연한 협업 및 커뮤니케이션
    """)

with tab2:
    st.subheader("🎯 미래의 나를 향한 로드맵")
    st.write("기술을 통해 세상에 긍정적인 임팩트를 주는 전문가로 성장하는 것이 저의 궁극적인 목표입니다.")
    st.progress(70, text="목표 달성도 진행 중!")
