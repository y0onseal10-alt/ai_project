import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="한국수력원자력 세금 분석",
    page_icon="💰",
    layout="wide"
)

st.title("💰 한국수력원자력 세금 납부 현황 분석")
st.markdown("---")

# -----------------------------------
# CSV 읽기
# -----------------------------------
def load_data():

    filename = "한국수력원자력(주)_세금납부 현황_20241231.csv"

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp949",
        "euc-kr"
    ]

    for enc in encodings:
        try:
            df = pd.read_csv(filename, encoding=enc)
            st.success(f"파일 읽기 성공 (인코딩: {enc})")
            return df
        except Exception:
            pass

    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# -----------------------------------
# 컬럼 확인
# -----------------------------------
st.subheader("🔍 데이터 확인")

st.write("컬럼명:")
st.write(df.columns.tolist())

# -----------------------------------
# 컬럼 자동 탐색
# -----------------------------------
year2023 = None
year2024 = None

for col in df.columns:

    if "2023" in str(col):
        year2023 = col

    if "2024" in str(col):
        year2024 = col

if year2023 is None or year2024 is None:

    st.error("2023 또는 2024 컬럼을 찾을 수 없습니다.")
    st.stop()

# -----------------------------------
# 숫자 변환
# -----------------------------------
df[year2023] = pd.to_numeric(
    df[year2023],
    errors="coerce"
)

df[year2024] = pd.to_numeric(
    df[year2024],
    errors="coerce"
)

# -----------------------------------
# 세목 컬럼 찾기
# -----------------------------------
if "세목" in df.columns:
    tax_col = "세목"
else:
    tax_col = df.columns[1]

# -----------------------------------
# 총액 계산
# -----------------------------------
total_2023 = df[year2023].sum()
total_2024 = df[year2024].sum()

increase = total_2024 - total_2023

increase_rate = round(
    increase / total_2023 * 100,
    2
)

# -----------------------------------
# 비율 계산
# -----------------------------------
df["2023비율"] = round(
    df[year2023] / total_2023 * 100,
    2
)

df["2024비율"] = round(
    df[year2024] / total_2024 * 100,
    2
)

# -----------------------------------
# KPI
# -----------------------------------
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

# -----------------------------------
# 세금 선택
# -----------------------------------
st.subheader("📊 세금 종류 선택")

tax_list = df[tax_col].unique()

selected_tax = st.selectbox(
    "세금 종류 선택",
    tax_list
)

selected = df[
    df[tax_col] == selected_tax
]

ratio_2023 = selected["2023비율"].iloc[0]
ratio_2024 = selected["2024비율"].iloc[0]

chart_df = pd.DataFrame({
    "연도": ["2023", "2024"],
    "비율": [ratio_2023, ratio_2024]
})

max_value = chart_df["비율"].max()

colors = []

for v in chart_df["비율"]:

    if v == max_value:
        colors.append("red")
    else:
        colors.append("#1E88E5")

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
    template="plotly_white",
    height=500,
    xaxis_title="연도",
    yaxis_title="비율 (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# -----------------------------------
# 순위 그래프
# -----------------------------------
st.subheader("📈 세금 종류별 비율 순위")

year_select = st.radio(
    "연도 선택",
    ["2023", "2024"],
    horizontal=True
)

ratio_col = f"{year_select}비율"

rank_df = (
    df.sort_values(
        ratio_col,
        ascending=False
    )
    .reset_index(drop=True)
)

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

bar_colors = ["red"]

for i in range(1, len(rank_df)):
    bar_colors.append(
        blue_gradient[
            min(i - 1, len(blue_gradient)-1)
        ]
    )

fig2 = px.bar(
    rank_df,
    x=tax_col,
    y=ratio_col,
    text=ratio_col
)

fig2.update_traces(
    marker_color=bar_colors,
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig2.update_layout(
    title=f"{year_select}년 세금 비율 순위",
    template="plotly_white",
    height=650
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------------
# 원그래프
# -----------------------------------
st.subheader("🥧 비율 구성")

fig3 = px.pie(
    rank_df,
    names=tax_col,
    values=ratio_col,
    hole=0.45
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------------
# 데이터
# -----------------------------------
st.subheader("📋 원본 데이터")

st.dataframe(
    df,
    use_container_width=True
)
