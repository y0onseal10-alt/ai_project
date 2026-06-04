import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="한국수력원자력 세금 분석",
    page_icon="💰",
    layout="wide"
)

st.title("💰 한국수력원자력 세금 납부 현황 분석")
st.markdown("---")

# CSV 불러오기
df = pd.read_csv("한국수력원자력(주)_세금납부 현황_20241231.csv", encoding="utf-8")

# 숫자형 변환
df["2023년"] = pd.to_numeric(df["2023년"], errors="coerce")
df["2024년"] = pd.to_numeric(df["2024년"], errors="coerce")

# 전체 합계
total_2023 = df["2023년"].sum()
total_2024 = df["2024년"].sum()

# 비율 계산
df["2023비율"] = round(df["2023년"] / total_2023 * 100, 2)
df["2024비율"] = round(df["2024년"] / total_2024 * 100, 2)

st.subheader("📊 세금 종류 선택")

tax_list = df["세목"].unique()

selected_tax = st.selectbox(
    "세금 종류를 선택하세요",
    tax_list
)

selected = df[df["세목"] == selected_tax]

ratio_2023 = selected["2023비율"].values[0]
ratio_2024 = selected["2024비율"].values[0]

chart_df = pd.DataFrame({
    "연도": ["2023", "2024"],
    "비율": [ratio_2023, ratio_2024]
})

# 최고값 찾기
max_value = chart_df["비율"].max()

colors = []

for v in chart_df["비율"]:
    if v == max_value:
        colors.append("red")
    else:
        colors.append("rgb(30,144,255)")

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df["연도"],
        y=chart_df["비율"],
        text=chart_df["비율"].astype(str) + "%",
        textposition="outside",
        marker_color=colors
    )
)

fig.update_layout(
    title=f"{selected_tax} 비율 비교",
    xaxis_title="연도",
    yaxis_title="전체 세금 중 비율 (%)",
    height=600,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("📈 전체 세금 비율 순위 (2024년)")

rank_df = df.sort_values(
    "2024비율",
    ascending=False
).reset_index(drop=True)

color_list = ["red"]

blue_gradient = [
    "#0d47a1",
    "#1565c0",
    "#1976d2",
    "#1e88e5",
    "#2196f3",
    "#42a5f5",
    "#64b5f6",
    "#90caf9"
]

for i in range(1, len(rank_df)):
    color_list.append(
        blue_gradient[min(i - 1, len(blue_gradient)-1)]
    )

fig2 = px.bar(
    rank_df,
    x="세목",
    y="2024비율",
    text="2024비율"
)

fig2.update_traces(
    marker_color=color_list,
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig2.update_layout(
    title="2024년 세금 종류별 비율 순위",
    xaxis_title="세목",
    yaxis_title="비율 (%)",
    height=700,
    template="plotly_white"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("📋 원본 데이터")

st.dataframe(
    df,
    use_container_width=True
)
