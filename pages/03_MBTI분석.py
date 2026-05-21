# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="세계 MBTI TOP10 분석",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌍 MBTI 유형별 국가 TOP 10")
st.markdown("MBTI 유형을 선택하면 비율이 가장 높은 국가 TOP 10을 보여줍니다.")

# -----------------------------------
# 데이터 로드
# -----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# -----------------------------------
# MBTI 리스트
# -----------------------------------
mbti_columns = [
    "INFJ", "ISFJ", "INTP", "ISFP",
    "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP",
    "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# -----------------------------------
# MBTI 선택
# -----------------------------------
selected_mbti = st.selectbox(
    "🧠 MBTI 유형 선택",
    mbti_columns
)

# -----------------------------------
# TOP 10 국가 추출
# -----------------------------------
top10 = (
    df[["Country", selected_mbti]]
    .sort_values(by=selected_mbti, ascending=False)
    .head(10)
    .reset_index(drop=True)
)

# 퍼센트 변환
top10[selected_mbti] = top10[selected_mbti] * 100

# -----------------------------------
# 색상 설정
# 1등 = 빨간색
# 나머지 = 파란색 그라데이션
# -----------------------------------
blue_scale = px.colors.sequential.Blues

colors = []

for i in range(len(top10)):
    if i == 0:
        colors.append("#ff2b2b")
    else:
        idx = min(i + 2, len(blue_scale) - 1)
        colors.append(blue_scale[idx])

# -----------------------------------
# TOP 국가 정보
# -----------------------------------
top_country = top10.iloc[0]["Country"]
top_value = top10.iloc[0][selected_mbti]

# -----------------------------------
# 상단 카드
# -----------------------------------
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "선택한 MBTI",
        selected_mbti
    )

with col2:
    st.metric(
        "🥇 1위 국가",
        top_country
    )

with col3:
    st.metric(
        "📈 최고 비율",
        f"{top_value:.2f}%"
    )

st.markdown("---")

# -----------------------------------
# Plotly 막대 그래프
# -----------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top10["Country"],
        y=top10[selected_mbti],
        marker=dict(
            color=colors,
            line=dict(
                color="white",
                width=1.5
            )
        ),
        text=[
            f"{v:.2f}%"
            for v in top10[selected_mbti]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        f"{selected_mbti}: " +
        "%{y:.2f}%<extra></extra>"
    )
)

# -----------------------------------
# 그래프 스타일
# -----------------------------------
fig.update_layout(
    title={
        "text": f"🌎 {selected_mbti} 비율이 높은 국가 TOP 10",
        "x": 0.5,
        "xanchor": "center"
    },
    template="plotly_white",
    height=700,
    xaxis_title="국가",
    yaxis_title="비율 (%)",
    hovermode="x unified",
    font=dict(
        size=15
    ),
    margin=dict(
        t=80,
        l=40,
        r=40,
        b=40
    )
)

fig.update_yaxes(
    showgrid=True,
    gridcolor="rgba(200,200,200,0.3)"
)

# -----------------------------------
# 그래프 출력
# -----------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------
# 원형 그래프
# -----------------------------------
st.markdown("## 🥧 TOP10 국가 비율 분포")

pie_fig = px.pie(
    top10,
    names="Country",
    values=selected_mbti,
    hole=0.45
)

pie_fig.update_traces(
    textposition='inside',
    textinfo='percent+label'
)

pie_fig.update_layout(
    height=650
)

st.plotly_chart(
    pie_fig,
    use_container_width=True
)

# -----------------------------------
# 데이터 테이블
# -----------------------------------
st.markdown("## 📋 상세 데이터")

display_df = top10.copy()
display_df[selected_mbti] = display_df[selected_mbti].round(2)

display_df.columns = ["국가", f"{selected_mbti} 비율(%)"]

st.dataframe(
    display_df,
    use_container_width=True
)

# -----------------------------------
# 푸터
# -----------------------------------
st.markdown("---")
st.caption("Made with Streamlit + Plotly")
