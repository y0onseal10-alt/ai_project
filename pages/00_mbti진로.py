import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천기 💼",
    page_icon="✨",
)

# MBTI별 추천 데이터
mbti_data = {
    "INTJ": {
        "jobs": [
            {
                "name": "데이터 분석가 📊",
                "major": "통계학과, 컴퓨터공학과",
                "personality": "논리적이고 계획 세우는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "건축가 🏛️",
                "major": "건축학과",
                "personality": "창의적이면서도 꼼꼼한 사람",
                "salary": "평균 연봉 약 5,000만 원"
            }
        ]
    },

    "INTP": {
        "jobs": [
            {
                "name": "프로그래머 💻",
                "major": "컴퓨터공학과",
                "personality": "혼자 깊게 생각하는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "연구원 🔬",
                "major": "생명과학과, 화학과",
                "personality": "호기심이 많고 탐구심이 강한 사람",
                "salary": "평균 연봉 약 4,800만 원"
            }
        ]
    },

    "ENTJ": {
        "jobs": [
            {
                "name": "CEO 👔",
                "major": "경영학과",
                "personality": "리더십이 강하고 추진력이 있는 사람",
                "salary": "평균 연봉 약 7,000만 원 이상"
            },
            {
                "name": "마케팅 기획자 📢",
                "major": "광고홍보학과",
                "personality": "전략적으로 생각하는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 4,500만 원"
            }
        ]
    },

    "ENTP": {
        "jobs": [
            {
                "name": "광고 기획자 🎨",
                "major": "광고홍보학과",
                "personality": "아이디어가 많고 새로운 걸 좋아하는 사람",
                "salary": "평균 연봉 약 4,300만 원"
            },
            {
                "name": "유튜브 크리에이터 🎥",
                "major": "미디어학과",
                "personality": "재치 있고 사람들과 소통을 좋아하는 사람",
                "salary": "수익 편차가 매우 큼"
            }
        ]
    },

    "INFJ": {
        "jobs": [
            {
                "name": "심리상담사 💚",
                "major": "심리학과",
                "personality": "공감 능력이 뛰어난 사람",
                "salary": "평균 연봉 약 3,800만 원"
            },
            {
                "name": "작가 ✍️",
                "major": "문예창작과",
                "personality": "감수성이 풍부하고 상상력이 좋은 사람",
                "salary": "수익 편차가 큼"
            }
        ]
    },

    "INFP": {
        "jobs": [
            {
                "name": "일러스트레이터 🎨",
                "major": "시각디자인과",
                "personality": "감성이 풍부하고 창의적인 사람",
                "salary": "평균 연봉 약 3,500만 원"
            },
            {
                "name": "작곡가 🎵",
                "major": "실용음악과",
                "personality": "예술적 감각이 뛰어난 사람",
                "salary": "수익 편차가 큼"
            }
        ]
    },

    "ENFJ": {
        "jobs": [
            {
                "name": "교사 🍎",
                "major": "교육학과",
                "personality": "사람을 잘 이끌고 배려심이 많은 사람",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "승무원 ✈️",
                "major": "항공서비스학과",
                "personality": "친절하고 소통 능력이 좋은 사람",
                "salary": "평균 연봉 약 4,000만 원"
            }
        ]
    },

    "ENFP": {
        "jobs": [
            {
                "name": "방송인 🎤",
                "major": "방송연예과",
                "personality": "에너지가 넘치고 밝은 사람",
                "salary": "수익 편차가 큼"
            },
            {
                "name": "기획자 💡",
                "major": "경영학과",
                "personality": "아이디어가 많고 활동적인 사람",
                "salary": "평균 연봉 약 4,500만 원"
            }
        ]
    },

    "ISTJ": {
        "jobs": [
            {
                "name": "공무원 🏢",
                "major": "행정학과",
                "personality": "책임감이 강하고 성실한 사람",
                "salary": "평균 연봉 약 4,000만 원"
            },
            {
                "name": "회계사 🧾",
                "major": "회계학과",
                "personality": "꼼꼼하고 체계적인 사람",
                "salary": "평균 연봉 약 6,000만 원"
            }
        ]
    },

    "ISFJ": {
        "jobs": [
            {
                "name": "간호사 🏥",
                "major": "간호학과",
                "personality": "배려심이 많고 책임감 있는 사람",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "유치원 교사 🧸",
                "major": "유아교육과",
                "personality": "다정하고 인내심 있는 사람",
                "salary": "평균 연봉 약 3,500만 원"
            }
        ]
    },

    "ESTJ": {
        "jobs": [
            {
                "name": "경찰관 🚔",
                "major": "경찰행정학과",
                "personality": "정의감이 강하고 리더십 있는 사람",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "은행원 💳",
                "major": "경제학과",
                "personality": "책임감 있고 현실적인 사람",
                "salary": "평균 연봉 약 5,000만 원"
            }
        ]
    },

    "ESFJ": {
        "jobs": [
            {
                "name": "호텔리어 🏨",
                "major": "호텔관광학과",
                "personality": "친절하고 사람 만나는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 3,800만 원"
            },
            {
                "name": "간호사 💉",
                "major": "간호학과",
                "personality": "배려심이 많고 성실한 사람",
                "salary": "평균 연봉 약 4,500만 원"
            }
        ]
    },

    "ISTP": {
        "jobs": [
            {
                "name": "파일럿 🛫",
                "major": "항공운항학과",
                "personality": "침착하고 상황 판단이 빠른 사람",
                "salary": "평균 연봉 약 8,000만 원"
            },
            {
                "name": "자동차 엔지니어 🚗",
                "major": "기계공학과",
                "personality": "기계를 다루는 걸 좋아하는 사람",
                "salary": "평균 연봉 약 5,500만 원"
            }
        ]
    },

    "ISFP": {
        "jobs": [
            {
                "name": "플로리스트 🌸",
                "major": "원예학과",
                "personality": "감각적이고 섬세한 사람",
                "salary": "평균 연봉 약 3,000만 원"
            },
            {
                "name": "메이크업 아티스트 💄",
                "major": "뷰티학과",
                "personality": "예술 감각이 뛰어난 사람",
                "salary": "평균 연봉 약 3,500만 원"
            }
        ]
    },

    "ESTP": {
        "jobs": [
            {
                "name": "스포츠 트레이너 🏋️",
                "major": "체육학과",
                "personality": "활동적이고 에너지 넘치는 사람",
                "salary": "평균 연봉 약 3,800만 원"
            },
            {
                "name": "영업 전문가 📞",
                "major": "경영학과",
                "personality": "사교성이 좋고 도전적인 사람",
                "salary": "평균 연봉 약 5,000만 원"
            }
        ]
    },

    "ESFP": {
        "jobs": [
            {
                "name": "배우 🎭",
                "major": "연극영화과",
                "personality": "표현력이 좋고 밝은 사람",
                "salary": "수익 편차가 큼"
            },
            {
                "name": "파티시에 🍰",
                "major": "제과제빵학과",
                "personality": "손재주가 좋고 감각적인 사람",
                "salary": "평균 연봉 약 3,500만 원"
            }
        ]
    }
}

st.title("✨ MBTI 진로 추천기 ✨")
st.write("나의 MBTI에 어울리는 진로를 알아보자! 😆")

selected_mbti = st.selectbox(
    "👉 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

if st.button("추천 보기 💖"):
    st.subheader(f"🎉 {selected_mbti} 유형 추천 진로")

    jobs = mbti_data[selected_mbti]["jobs"]

    for job in jobs:
        st.markdown("---")
        st.header(job["name"])
        st.write(f"📚 **추천 학과:** {job['major']}")
        st.write(f"🧠 **어울리는 성격:** {job['personality']}")
        st.write(f"💰 **평균 연봉:** {job['salary']}")

    st.success("✨ 재미로 보는 추천이니까 너무 과몰입은 금지~!")
