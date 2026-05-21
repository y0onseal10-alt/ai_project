# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="세계 국가 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("🌍 국가별 MBTI 성향 분석")
st.markdown("국가를 선택하면 MBTI 비율을 인터랙티브 그래프로 보여줍니다.")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------
# MBTI 컬럼 추출
# -----------------------------
mbti_columns = [
    "INFJ", "ISFJ", "INTP", "ISFP",
    "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP",
    "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# -----------------------------
# 국가 선택
# -----------------------------
country = st.selectbox(
    "🌎 국가 선택",
    sorted(df["Country"].unique())
)

# -----------------------------
# 선택 국가 데이터
# -----------------------------
selected = df[df["Country"] == country]

# MBTI 비율
values = selected[mbti_columns].iloc[0]

# 데이터프레임 변환
chart_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "비율": values.values
})

# 퍼센트 변환
chart_df["비율"] = chart_df["비율"] * 100

# 정렬
chart_df = chart_df.sort_values(
    by="비율",
    ascending=False
).reset_index(drop=True)

# -----------------------------
# 색상 설정
# 1등 = 빨강
# 나머지 = 파랑 그라데이션
# -----------------------------
colors = []

blue_scale = px.colors.sequential.Blues

for i in range(len(chart_df)):
    if i == 0:
        colors.append("#ff2b2b")
    else:
        idx = min(i + 2, len(blue_scale) - 1)
        colors.append(blue_scale[idx])

# -----------------------------
# 최고 MBTI
# -----------------------------
top_mbti = chart_df.iloc[0]["MBTI"]
top_value = chart_df.iloc[0]["비율"]

# -----------------------------
# 카드 UI
# -----------------------------
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.metric(
        label="🥇 가장 높은 MBTI",
        value=top_mbti
    )

with col2:
    st.metric(
        label="📊 비율",
        value=f"{top_value:.2f}%"
    )

st.markdown("---")

# -----------------------------
# Plotly 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df["MBTI"],
        y=chart_df["비율"],
        marker=dict(
            color=colors,
            line=dict(
                color="white",
                width=1
            )
        ),
        text=[
            f"{v:.2f}%"
            for v in chart_df["비율"]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2f}%<extra></extra>"
    )
)

# -----------------------------
# 그래프 스타일
# -----------------------------
fig.update_layout(
    title={
        "text": f"📈 {country} MBTI 비율 분석",
        "x": 0.5,
        "xanchor": "center"
    },
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    template="plotly_white",
    height=650,
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

# -----------------------------
# 그래프 출력
# -----------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# 원형 그래프 추가
# -----------------------------
st.markdown("## 🥧 MBTI 비율 분포")

pie_fig = px.pie(
    chart_df,
    names="MBTI",
    values="비율",
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

# -----------------------------
# 데이터 테이블
# -----------------------------
st.markdown("## 📋 상세 데이터")

display_df = chart_df.copy()
display_df["비율"] = display_df["비율"].round(2)

st.dataframe(
    display_df,
    use_container_width=True
)

# -----------------------------
# 푸터
# -----------------------------
st.markdown("---")
st.caption("Made with Streamlit + Plotly")
