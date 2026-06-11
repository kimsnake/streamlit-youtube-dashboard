# Streamlit YouTube Dashboard

YouTube 채널 데이터를 시각화하는 인터랙티브 대시보드입니다.  
Streamlit과 Neon Postgres를 사용하여 자동 수집된 채널 지표를 월별로 분석할 수 있습니다.
포트폴리오용으로 제작된 가벼운 프로젝트입니다.

## 🔗 Live Demo

> 배포 후 아래 링크를 추가해주세요  
> [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

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

## 📊 프로젝트 구조
- streamlit-youtube-dashboard/
- ├── streamlit_app.py          # 메인 대시보드 코드
- ├── requirements.txt
- └── README.md

## 🗄 데이터베이스
Neon Postgres (무료 티어 사용)
자동 수집된 YouTube 채널 데이터 (조회수, 구독자, 좋아요, 시청 시간 등)