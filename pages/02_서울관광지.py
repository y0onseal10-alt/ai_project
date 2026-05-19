import streamlit as st
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
            icon="star"
        )
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 리스트 출력
st.subheader("📌 관광지 목록")

for idx, place in enumerate(places, start=1):
    st.markdown(f"**{idx}. {place['name']}** - {place['desc']}")
