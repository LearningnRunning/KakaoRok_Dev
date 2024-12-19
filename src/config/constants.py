import streamlit as st

LOGO_IMG_PATH = "./static/img/what2eat-logo-middle.png"
LOGO_SMALL_IMG_PATH = "./static/img/what2eat-logo-small.png"
LOGO_TITLE_IMG_PATH = "./static/img/what2eat-word-logo-small.png"
GUIDE_IMG_PATH = "./static/img/kakomap_nickname_guide.jpg"

DEFAULT_ADDRESS_INFO_LIST = ["강남구 삼성동", 127.0567474, 37.5074423]

DINER_REVIEW_AVG = 3.2

DATA_PATH = "./data/seoul_data/*.csv"
MODEL_PATH = "./data/model_data"

# Kakao API settings
KAKAO_API_URL = "https://dapi.kakao.com/v2/local/search/keyword.json"
KAKAO_API_HEADERS = {"Authorization": f"KakaoAK {st.secrets['REST_API_KEY']}"}

# 우선순위를 정의
PRIORITY_ORDER = {"한식": 1, "중식": 2, "일식": 2, "양식": 2}


ZONE_INDEX = {
    "서울 강북권": 0,
    "서울 강남권": 1,
    "서울 서부권": 2,
    "경기 동부권": 3,
    "경기 서부권": 4,
    "경기 중부권": 5,
    "강원 동부권": 6,
    "강원 중부권": 7,
    "경북 동부권": 8,
    "인천권": 9,
    "제주권": 10,
    "광주권": 11,
}

CITY_INDEX = {
    0: "강원특별자치도 강릉시",
    1: "강원특별자치도 고성군",
    2: "강원특별자치도 동해시",
    3: "강원특별자치도 속초시",
    4: "강원특별자치도 양양군",
    5: "강원특별자치도 평창군",
    6: "경기 고양시",
    7: "경기 과천시",
    8: "경기 광명시",
    9: "경기 광주시",
    10: "경기 구리시",
    11: "경기 김포시",
    12: "경기 남양주시",
    13: "경기 부천시",
    14: "경기 성남시",
    15: "경기 시흥시",
    16: "경기 안양시",
    17: "경기 용인시",
    18: "경기 하남시",
    19: "경북 포항시",
    20: "광주 광산구",
    21: "광주 남구",
    22: "광주 동구",
    23: "광주 북구",
    24: "광주 서구",
    25: "서울 강남구",
    26: "서울 강동구",
    27: "서울 강북구",
    28: "서울 강서구",
    29: "서울 관악구",
    30: "서울 광진구",
    31: "서울 구로구",
    32: "서울 금천구",
    33: "서울 노원구",
    34: "서울 도봉구",
    35: "서울 동대문구",
    36: "서울 동작구",
    37: "서울 마포구",
    38: "서울 서대문구",
    39: "서울 서초구",
    40: "서울 성동구",
    41: "서울 성북구",
    42: "서울 송파구",
    43: "서울 양천구",
    44: "서울 영등포구",
    45: "서울 용산구",
    46: "서울 은평구",
    47: "서울 종로구",
    48: "서울 중구",
    49: "서울 중랑구",
    50: "인천 계양구",
    51: "전남 나주시",
    52: "전남 담양군",
    53: "전남 장성군",
    54: "제주특별자치도 서귀포시",
    55: "제주특별자치도 제주시",
}
