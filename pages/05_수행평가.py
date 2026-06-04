@st.cache_data
def load_data():

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp949",
        "euc-kr"
    ]

    for enc in encodings:
        try:
            df = pd.read_csv(
                "한국수력원자력(주)_세금납부 현황_20241231.csv",
                encoding=enc
            )
            return df
        except:
            pass

    st.error("CSV 파일 인코딩을 읽을 수 없습니다.")
    st.stop()
    
