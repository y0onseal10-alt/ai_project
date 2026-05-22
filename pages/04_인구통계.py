import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="서울시 인구통계",
    layout="wide"
)

# ---------------------------
# 한글 폰트 설정
# ---------------------------
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Malgun Gothic', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# 데이터 불러오기
# ---------------------------
df = pd.read_csv("population.csv")

# 첫 번째 컬럼 이름 변경
df.rename(columns={df.columns[0]: "행정구역"}, inplace=True)

# 연령 컬럼
age_columns = df.columns[1:]

# ---------------------------
# 제목
# ---------------------------
st.title("서울시의 인구통계")

# ---------------------------
# 행정구 선택
# ---------------------------
district = st.selectbox(
    "행정구를 선택하세요",
    df["행정구역"]
)

# 선택 데이터
selected_row = df[df["행정구역"] == district]

# 값 추출
population_values = selected_row[age_columns].values.flatten()

# ---------------------------
# Plotly 그래프
# ---------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=age_columns,
        y=population_values,
        mode='lines+markers',
        line=dict(
            color='red',
            width=4
        ),
        marker=dict(
            size=8,
            color='red'
        )
    )
)

# 그래프 스타일
fig.update_layout(
    title={
        'text': "서울시의 인구통계",
        'x': 0.5,
        'xanchor': 'center'
    },
    xaxis_title="연령대",
    yaxis_title="인구수",
    plot_bgcolor="#EBDCFF",   # 연한 보라색
    paper_bgcolor="#EBDCFF",
    font=dict(
        family="Malgun Gothic",
        size=15,
        color="black"
    ),
    height=650
)

# 출력
st.plotly_chart(fig, use_container_width=True)
