

import streamlit as st

st.set_page_config(
    page_title="MBTI 음악 & 진로 추천",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI 음악 & 진로 추천")
st.subheader("나의 성격에 어울리는 음악과 미래의 직업은?")
st.write("MBTI를 선택하면 어울리는 음악 2곡과 진로를 추천해 줄게! ✨")

mbti_data = {
    "ISTJ": {
        "music": ["폴킴 - 모든 날, 모든 순간", "아이유 - 밤편지"],
        "personality": "책임감이 강하고 계획적이며 꼼꼼한 성격!",
        "career": ["회계사", "공무원", "연구원", "경영관리자"],
        "major": ["경영학과", "회계학과", "행정학과", "통계학과"]
    },
    "ISFJ": {
        "music": ["성시경 - 너의 모든 순간", "AKMU - 어떻게 이별까지 사랑하겠어"],
        "personality": "따뜻하고 배려심이 많으며 주변 사람을 잘 챙기는 성격!",
        "career": ["교사", "간호사", "사회복지사", "호텔리어"],
        "major": ["교육학과", "간호학과", "사회복지학과", "호텔관광학과"]
    },
    "INFJ": {
        "music": ["아이유 - 이름에게", "BTS - 봄날"],
        "personality": "생각이 깊고 공감 능력이 뛰어나며 가치관이 뚜렷한 성격!",
        "career": ["상담사", "작가", "교사", "기획자"],
        "major": ["심리학과", "국어국문학과", "교육학과", "광고홍보학과"]
    },
    "INTJ": {
        "music": ["D.O. - 괜찮아도 괜찮아", "백예린 - Square"],
        "personality": "분석적이고 독립적이며 목표를 세워 실행하는 성격!",
        "career": ["개발자", "건축가", "연구원", "전략기획자"],
        "major": ["컴퓨터공학과", "건축학과", "수학과", "산업공학과"]
    },
    "ISTP": {
        "music": ["DEAN - instagram", "Crush - Beautiful"],
        "personality": "실용적이고 호기심이 많으며 문제 해결을 잘하는 성격!",
        "career": ["요리사", "기술자", "정비사", "프로그래머"],
        "major": ["조리학과", "기계공학과", "컴퓨터공학과", "자동차공학과"]
    },
    "ISFP": {
        "music": ["10CM - 폰서트", "볼빨간사춘기 - 여행"],
        "personality": "감수성이 풍부하고 자유로우며 자신만의 감각이 있는 성격!",
        "career": ["디자이너", "요리사", "사진작가", "플로리스트"],
        "major": ["시각디자인학과", "조리학과", "사진학과", "원예학과"]
    },
    "INFP": {
        "music": ["아이유 - 마음", "AKMU - 시간과 낙엽"],
        "personality": "상상력이 풍부하고 감성적이며 자신만의 가치관을 중요하게 생각하는 성격!",
        "career": ["작가", "일러스트레이터", "상담사", "예술가"],
        "major": ["문예창작학과", "미술학과", "심리학과", "디자인학과"]
    },
    "INTP": {
        "music": ["혁오 - TOMBOY", "Lauv - I Like Me Better"],
        "personality": "호기심이 많고 논리적이며 새로운 지식을 탐구하는 성격!",
        "career": ["과학자", "개발자", "연구원", "데이터 분석가"],
        "major": ["물리학과", "컴퓨터공학과", "수학과", "데이터사이언스학과"]
    },
    "ESTP": {
        "music": ["싸이 - 챔피언", "세븐틴 - 아주 NICE"],
        "personality": "활동적이고 도전적이며 새로운 경험을 즐기는 성격!",
        "career": ["사업가", "마케팅 전문가", "운동선수", "이벤트 기획자"],
        "major": ["경영학과", "스포츠과학과", "광고홍보학과", "이벤트학과"]
    },
    "ESFP": {
        "music": ["워너원 - 에너제틱", "아이브 - After LIKE"],
        "personality": "밝고 사교적이며 사람들과 어울리는 것을 좋아하는 성격!",
        "career": ["셰프", "방송인", "파티플래너", "서비스 전문가"],
        "major": ["호텔조리학과", "외식경영학과", "방송연예과", "호텔관광학과"]
    },
    "ENFP": {
        "music": ["DAY6 - 한 페이지가 될 수 있게", "아이브 - I AM"],
        "personality": "열정적이고 창의적이며 새로운 아이디어가 넘치는 성격!",
        "career": ["콘텐츠 기획자", "마케터", "창업가", "배우"],
        "major": ["미디어학과", "경영학과", "광고홍보학과", "연극영화과"]
    },
    "ENTP": {
        "music": ["지코 - 아무노래", "NewJeans - Super Shy"],
        "personality": "재치 있고 도전적이며 토론과 새로운 시도를 좋아하는 성격!",
        "career": ["기업가", "변호사", "마케터", "기획자"],
        "major": ["경영학과", "법학과", "광고홍보학과", "창업학과"]
    },
    "ESTJ": {
        "music": ["BIGBANG - 뱅뱅뱅", "DAY6 - Welcome to the Show"],
        "personality": "리더십이 있고 체계적이며 책임감이 강한 성격!",
        "career": ["경영자", "경찰관", "관리자", "프로젝트 매니저"],
        "major": ["경영학과", "경찰행정학과", "행정학과", "산업공학과"]
    },
    "ESFJ": {
        "music": ["소녀시대 - 힘내!", "태연 - Weekend"],
        "personality": "친절하고 사교적이며 사람들과 협력하는 것을 좋아하는 성격!",
        "career": ["교사", "호텔리어", "승무원", "인사담당자"],
        "major": ["교육학과", "호텔관광학과", "항공서비스학과", "경영학과"]
    },
    "ENFJ": {
        "music": ["윤하 - 사건의 지평선", "DAY6 - 예뻤어"],
        "personality": "공감 능력이 뛰어나고 사람들을 이끄는 것을 좋아하는 성격!",
        "career": ["교사", "상담사", "인사관리자", "사회복지사"],
        "major": ["교육학과", "심리학과", "사회복지학과", "경영학과"]
    },
    "ENTJ": {
        "music": ["BTS - ON", "에스파 - Drama"],
        "personality": "목표 지향적이고 추진력이 강하며 리더십이 있는 성격!",
        "career": ["CEO", "변호사", "경영컨설턴트", "사업가"],
        "major": ["경영학과", "경제학과", "법학과", "산업공학과"]
    }
}

mbti = st.selectbox(
    "💫 나의 MBTI를 선택해 줘!",
    list(mbti_data.keys())
)

if st.button("🎵 나의 추천 결과 확인하기", use_container_width=True):

    result = mbti_data[mbti]

    st.divider()

    st.header(f"🌟 {mbti} 유형 분석")

    st.subheader("💖 나의 성격")
    st.info(result["personality"])

    st.subheader("🎧 추천 음악 TOP 2")
    for i, song in enumerate(result["music"], 1):
        st.write(f"**{i}. {song}**")

    st.subheader("💼 추천 진로")
    for career in result["career"]:
        st.write(f"✨ {career}")

    st.subheader("🎓 관련 학과")
    for major in result["major"]:
        st.write(f"📚 {major}")

    st.divider()

    st.success(
        "나만의 장점을 발견하고 꿈을 향해 한 걸음씩 나아가 보자! 🚀"
    )

    st.caption(
        "※ MBTI는 재미와 자기 이해를 위한 참고 자료야. "
        "실제 성격과 진로 선택은 개인의 관심사와 경험에 따라 달라질 수 있어!"
    )

st.divider()
st.caption("Made with ❤️ | MBTI MUSIC & CAREER")
