import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="한국수력원자력 세금 분석",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("💰 한국수력원자력 세금 납부 현황 분석")
st.markdown("---")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "한국수력원자력(주)_세금납부 현황_20241231.csv",
        encoding="utf-8-sig"
    )
    return df

df = load_data()

# 숫자형 변환
df["2023 납부액(억원)"] = pd.to_numeric(
    df["2023 납부액(억원)"],
    errors="coerce"
)

df["2024 납부액(억원)"] = pd.to_numeric(
    df["2024 납부액(억원)"],
    errors="coerce"
)

# -----------------------------
# 총합 계산
# -----------------------------
total_2023 = df["2023 납부액(억원)"].sum()
total_2024 = df["2024 납부액(억원)"].sum()

increase = total_2024 - total_2023
increase_rate = round(increase / total_2023 * 100, 2)

# 비율 계산
df["2023 비율"] = round(
    df["2023 납부액(억원)"] / total_2023 * 100,
    2
)

df["2024 비율"] = round(
    df["2024 납부액(억원)"] / total_2024 * 100,
    2
)

# -----------------------------
# KPI 카드
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "2023 총 세금",
    f"{total_2023:,.0f}억원"
)

col2.metric(
    "2024 총 세금",
    f"{total_2024:,.0f}억원"
)

col3.metric(
    "증가율",
    f"{increase_rate}%"
)

st.markdown("---")

# -----------------------------
# 세금 선택
# -----------------------------
st.subheader("📊 세금 종류 선택")

tax_list = df["세목"].unique()

selected_tax = st.selectbox(
    "세금 종류를 선택하세요",
    tax_list
)

selected = df[df["세목"] == selected_tax]

ratio_2023 = selected["2023 비율"].values[0]
ratio_2024 = selected["2024 비율"].values[0]

chart_df = pd.DataFrame({
    "연도": ["2023", "2024"],
    "비율": [ratio_2023, ratio_2024]
})

max_value = chart_df["비율"].max()

colors = []

for value in chart_df["비율"]:
    if value == max_value:
        colors.append("red")
    else:
        colors.append("#1E88E5")

# -----------------------------
# 선택 세금 그래프
# -----------------------------
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
    template="plotly_white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# 연도 선택
# -----------------------------
st.subheader("📈 세금 종류별 비율 순위")

year_option = st.radio(
    "연도 선택",
    ["2023", "2024"],
    horizontal=True
)

ratio_col = f"{year_option} 비율"

rank_df = (
    df.sort_values(
        ratio_col,
        ascending=False
    )
    .reset_index(drop=True)
)

# 색상
blue_gradient = [
    "#0D47A1",
    "#1565C0",
    "#1976D2",
    "#1E88E5",
    "#2196F3",
    "#42A5F5",
    "#64B5F6",
    "#90CAF9"
]

color_list = ["red"]

for i in range(1, len(rank_df)):
    color_list.append(
        blue_gradient[
            min(i - 1, len(blue_gradient) - 1)
        ]
    )

fig2 = px.bar(
    rank_df,
    x="세목",
    y=ratio_col,
    text=ratio_col
)

fig2.update_traces(
    marker_color=color_list,
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig2.update_layout(
    title=f"{year_option}년 세금 종류별 비율 순위",
    xaxis_title="세목",
    yaxis_title="비율 (%)",
    template="plotly_white",
    height=650
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------
# 원그래프
# -----------------------------
st.markdown("---")
st.subheader("🥧 세금 비율 구성")

fig3 = px.pie(
    rank_df,
    names="세목",
    values=ratio_col,
    hole=0.4
)

fig3.update_layout(
    height=600
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------
# 데이터 보기
# -----------------------------
st.markdown("---")
st.subheader("📋 원본 데이터")

st.dataframe(
    df,
    use_container_width=True
)
