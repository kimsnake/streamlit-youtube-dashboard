# Streamlit YouTube Dashboard

YouTube 채널 데이터를 시각화하는 인터랙티브 대시보드입니다.  
Streamlit과 Neon Postgres를 사용하여 자동 수집된 채널 지표를 월별로 분석할 수 있습니다.  
포트폴리오용으로 제작된 가벼운 프로젝트입니다.

## 🔗 Live Demo

[Live Demo](https://app-youtube-dashboard-ylqdapjb7ypkcnl2endvpw.streamlit.app/)

## ✨ 주요 기능

- 월별 데이터 필터링 (`2026-06`, `2026-07` 등)
- 6개의 주요 지표 시각화
  - 조회수 추이
  - 구독자 증가 추이
  - 좋아요 / 댓글 추이
  - 평균 시청 시간
  - 평균 시청 유지율
- 한글 지원 테이블
- Plotly 기반 인터랙티브 차트

## 🛠 기술 스택

- **Frontend**: Streamlit, Plotly
- **Database**: Neon Postgres (Serverless PostgreSQL)
- **Data Processing**: pandas
- **Deployment**: Streamlit Community Cloud
- **AI** : Grok

## 📊 프로젝트 구조
- streamlit-youtube-dashboard/
- ├── streamlit_app.py          # 메인 대시보드 코드
- ├── requirements.txt
- └── README.md

## 🗄 데이터베이스
- **Neon Postgres** (무료 티어 사용)
- 주요 수집 지표: 조회수, 구독자 증가, 좋아요, 댓글, 평균 시청 시간, 시청 유지율 등

## ⚠️ Limitations

- **노출수(Impressions) 및 CTR 자동 수집 미지원**  
  YouTube Data API에서는 impressions와 CTR을 제공하지 않으며, YouTube Analytics API를 사용하더라도 구현이 상당히 번거로웠습니다.
  따라서 현재는 해당 지표를 **수동으로 입력**하고 있으며, 대시보드에 그래프로 표시하지는 않고 있습니다.

- **향후 개선 계획**  
  필요에 따라 impressions와 CTR도 수동 입력 후 그래프로 표시하는 기능을 추가할 수 있습니다.

## 📌 비고

이 프로젝트는 포트폴리오 목적으로 제작되었으며, 실제 운영 환경에서의 고성능·고가용성을 목표로 하지는 않습니다.

