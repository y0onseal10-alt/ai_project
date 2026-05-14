import streamlit as st

st.set_page_config(
    page_title="MBTI 연애 궁합 💘",
    page_icon="💕",
)

# MBTI 연애 궁합 데이터
mbti_love = {
    "INTJ": [
        {
            "match": "ENFP 💖",
            "love_style": "서로 다른 매력으로 끌리는 영화 같은 연애 🎬",
            "personality": "밝고 긍정적이며 리액션 좋은 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        },
        {
            "match": "ENTP ⚡",
            "love_style": "티키타카 잘 되는 재밌는 연애 😆",
            "personality": "아이디어 많고 대화 잘 통하는 사람",
            "period": "평균 연애 기간 💕 약 1~2년"
        }
    ],

    "INTP": [
        {
            "match": "ENTJ 👑",
            "love_style": "서로 부족한 부분을 채워주는 연애 🧩",
            "personality": "리더십 있고 추진력 있는 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ENFJ 🌷",
            "love_style": "감정적으로 안정감을 주는 연애 ☁️",
            "personality": "배려심 많고 따뜻한 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        }
    ],

    "ENTJ": [
        {
            "match": "INFP 🌙",
            "love_style": "서로에게 새로운 시각을 알려주는 연애 ✨",
            "personality": "감성적이고 공감 잘하는 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "INTP 🧠",
            "love_style": "대화가 끊이지 않는 지적인 연애 📚",
            "personality": "생각이 깊고 호기심 많은 사람",
            "period": "평균 연애 기간 💕 약 1~3년"
        }
    ],

    "ENTP": [
        {
            "match": "INFJ 💞",
            "love_style": "서로 자극 주며 성장하는 연애 🌱",
            "personality": "차분하면서 속이 깊은 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "INTJ 🔥",
            "love_style": "밀당 없이 솔직한 연애 😎",
            "personality": "논리적이고 똑똑한 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        }
    ],

    "INFJ": [
        {
            "match": "ENTP 🎈",
            "love_style": "서로에게 없는 매력을 느끼는 연애 💫",
            "personality": "유쾌하고 장난기 많은 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ENFP 🌸",
            "love_style": "감정 표현이 풍부한 설레는 연애 💌",
            "personality": "따뜻하고 표현 잘하는 사람",
            "period": "평균 연애 기간 💕 약 3년"
        }
    ],

    "INFP": [
        {
            "match": "ENFJ 🫶",
            "love_style": "서로를 다정하게 챙겨주는 연애 ☁️",
            "personality": "공감 능력 뛰어나고 따뜻한 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        },
        {
            "match": "ENTJ 🚀",
            "love_style": "현실감과 감성을 균형 있게 맞추는 연애 ⚖️",
            "personality": "목표 의식 강한 사람",
            "period": "평균 연애 기간 💕 약 2년"
        }
    ],

    "ENFJ": [
        {
            "match": "INFP 🌼",
            "love_style": "감성 가득한 드라마 같은 연애 🎞️",
            "personality": "배려심 깊고 순수한 사람",
            "period": "평균 연애 기간 💕 약 3년"
        },
        {
            "match": "ISFP 🎨",
            "love_style": "편안하고 안정감 있는 연애 🛋️",
            "personality": "다정하고 감각적인 사람",
            "period": "평균 연애 기간 💕 약 2년"
        }
    ],

    "ENFP": [
        {
            "match": "INTJ 🖤",
            "love_style": "반대 매력으로 끌리는 연애 🧲",
            "personality": "시크하지만 속정 깊은 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        },
        {
            "match": "INFJ 🌟",
            "love_style": "감정 교류가 풍부한 연애 💌",
            "personality": "섬세하고 이해심 많은 사람",
            "period": "평균 연애 기간 💕 약 2년"
        }
    ],

    "ISTJ": [
        {
            "match": "ESFP 🎉",
            "love_style": "서로에게 새로운 재미를 알려주는 연애 😆",
            "personality": "밝고 활발한 사람",
            "period": "평균 연애 기간 💕 약 1~2년"
        },
        {
            "match": "ESTP 🏍️",
            "love_style": "현실적이면서도 설레는 연애 💓",
            "personality": "행동력 강한 사람",
            "period": "평균 연애 기간 💕 약 2년"
        }
    ],

    "ISFJ": [
        {
            "match": "ESFP 🌈",
            "love_style": "서로를 행복하게 해주는 달달한 연애 🍭",
            "personality": "애교 많고 밝은 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ESTP 🚗",
            "love_style": "소소한 데이트를 즐기는 연애 🍀",
            "personality": "활동적이고 센스 있는 사람",
            "period": "평균 연애 기간 💕 약 1~3년"
        }
    ],

    "ESTJ": [
        {
            "match": "ISFP 🌷",
            "love_style": "현실과 감성이 조화로운 연애 🎵",
            "personality": "차분하고 감각적인 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ISTP 🔧",
            "love_style": "편하고 안정감 있는 연애 🧸",
            "personality": "무심한 듯 챙겨주는 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        }
    ],

    "ESFJ": [
        {
            "match": "ISFP 💐",
            "love_style": "서로를 다정하게 챙기는 연애 🫶",
            "personality": "부드럽고 따뜻한 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ISTP 🛵",
            "love_style": "편안하고 자연스러운 연애 🌿",
            "personality": "쿨하면서 배려심 있는 사람",
            "period": "평균 연애 기간 💕 약 1~2년"
        }
    ],

    "ISTP": [
        {
            "match": "ESFJ 🍓",
            "love_style": "서로 부족한 감정을 채워주는 연애 💞",
            "personality": "표현 잘하고 다정한 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ESTJ ⚙️",
            "love_style": "현실적이고 안정감 있는 연애 🏡",
            "personality": "책임감 강한 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        }
    ],

    "ISFP": [
        {
            "match": "ENFJ 🌸",
            "love_style": "감정을 잘 표현하는 따뜻한 연애 💌",
            "personality": "배려심 많고 다정한 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ESFJ 🍰",
            "love_style": "소소한 행복을 즐기는 연애 ☕",
            "personality": "친절하고 안정적인 사람",
            "period": "평균 연애 기간 💕 약 1~3년"
        }
    ],

    "ESTP": [
        {
            "match": "ISFJ 🌼",
            "love_style": "활발함과 안정감이 잘 맞는 연애 ⚡",
            "personality": "차분하고 배려심 많은 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ISTJ 📚",
            "love_style": "믿음이 중요한 현실적인 연애 🤝",
            "personality": "성실하고 책임감 있는 사람",
            "period": "평균 연애 기간 💕 약 2~3년"
        }
    ],

    "ESFP": [
        {
            "match": "ISFJ 🧸",
            "love_style": "달달하고 애정 표현 많은 연애 🍬",
            "personality": "다정하고 잘 챙겨주는 사람",
            "period": "평균 연애 기간 💕 약 2년"
        },
        {
            "match": "ISTJ 🖇️",
            "love_style": "서로 다른 성격이라 더 끌리는 연애 💘",
            "personality": "묵묵하지만 믿음직한 사람",
            "period": "평균 연애 기간 💕 약 1~3년"
        }
    ]
}

st.title("💘 MBTI 연애 궁합 추천기 💘")
st.write("내 MBTI와 잘 맞는 연애 상대를 알아보자 😳✨")

selected_mbti = st.selectbox(
    "👉 내 MBTI 선택하기!",
    list(mbti_love.keys())
)

if st.button("궁합 보기 💕"):
    st.subheader(f"✨ {selected_mbti}와 잘 맞는 MBTI ✨")

    matches = mbti_love[selected_mbti]

    for match in matches:
        st.markdown("---")
        st.header(match["match"])
        st.write(f"💌 **추천 연애 스타일:** {match['love_style']}")
        st.write(f"🧠 **잘 맞는 성격:** {match['personality']}")
        st.write(f"⏳ **평균 연애 기간:** {match['period']}")

    st.success("💖 MBTI 궁합은 재미로만 봐주기~! 진짜 중요한 건 서로 배려하는 마음 😆")
