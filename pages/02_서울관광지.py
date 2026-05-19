## app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP10",
    page_icon="📍",
    layout="wide"
)

st.title("📍 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("Folium 지도를 활용한 서울 관광 명소 시각화")

# 서울 주요 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 왕조의 대표 궁궐"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 먹거리 중심지"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.5665,
        "lon": 127.0092,
        "desc": "현대적 건축 랜드마크"
    },
    {
        "name": "인사동",
        "lat": 37.5740,
        "lon": 126.9850,
        "desc": "전통 문화와 기념품 거리"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "desc": "서울 최고층 랜드마크"
    },
    {
        "name": "한강공원",
        "lat": 37.5283,
        "lon": 126.9327,
        "desc": "서울 대표 휴식 공간"
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9996,
        "desc": "한국 전통 길거리 음식 명소"
    }
]

# 서울 중심 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=12,
    tiles="OpenStreetMap"
)

# 관광지 마커 추가
for idx, place in enumerate(places, start=1):
    popup_html = f"""
    <b>{idx}. {place['name']}</b><br>
    {place['desc']}
    """

    folium.Marker(
        location=[place['lat'], place['lon']],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=place['name'],
        icon=folium.Icon(
            color="red",
            icon="info-sign"
        )
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 리스트 출력
st.subheader("📌 관광지 목록")

for idx, place in enumerate(places, start=1):
    st.markdown(f"**{idx}. {place['name']}** - {place['desc']}")
```

---

## requirements.txt

```txt
streamlit
folium
streamlit-folium
```

---

# Streamlit Cloud 배포 방법

1. GitHub에 `app.py`와 `requirements.txt` 업로드
2. Streamlit Cloud 접속
3. GitHub 저장소 연결
4. Main file path를 `app.py`로 설정
5. Deploy 클릭

---

# 실행 명령어 (로컬 테스트)

```bash
streamlit run app.py
```
