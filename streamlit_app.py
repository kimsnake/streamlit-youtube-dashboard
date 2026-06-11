import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NightFocus Dashboard", layout="wide")

# 제목 + 채널 링크
st.markdown(
    """
    <h1>
        🎵 <a href="https://www.youtube.com/@NightFocusAudio_1H" target="_blank" style="text-decoration: none; color: inherit;">
        NightFocus Dashboard
        </a>
    </h1>
    """,
    unsafe_allow_html=True
)

conn = st.connection("neon", type="sql")

# ===================== 1. 월 목록 조회 (가볍게) =====================
months_df = conn.query("""
    SELECT DISTINCT TO_CHAR(date, 'YYYY-MM') as month
    FROM daily_channel_metrics
    ORDER BY month
""", ttl="10m")

months = months_df['month'].tolist()

if not months:
    st.warning("데이터가 없습니다.")
    st.stop()

selected_month = st.selectbox("📅 조회할 월 선택", months, index=len(months)-1)

# ===================== 2. 선택한 월 데이터만 조회 =====================
df = conn.query(f"""
    SELECT 
        date,
        views,
        subscribers_gained,
        likes,
        comments,
        average_view_duration,
        average_view_percentage
    FROM daily_channel_metrics
    WHERE TO_CHAR(date, 'YYYY-MM') = '{selected_month}'
    ORDER BY date
""", ttl="30m")

# ★ 중요: date를 datetime으로 변환
df['date'] = pd.to_datetime(df['date'])

st.subheader(f"📈 {selected_month} 채널 자동 수집 데이터 추이")

# ===================== 3열 그래프 =====================
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = px.line(df, x='date', y='views', title='1. 조회수 추이', markers=True)
    fig1.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig1, width="stretch", height=280)

with col2:
    fig2 = px.line(df, x='date', y='subscribers_gained', title='2. 구독자 증가 추이', markers=True)
    fig2.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig2, width="stretch", height=280)

with col3:
    fig3 = px.line(df, x='date', y='likes', title='3. 좋아요 추이', markers=True)
    fig3.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig3, width="stretch", height=280)

col4, col5, col6 = st.columns(3)

with col4:
    fig4 = px.line(df, x='date', y='comments', title='4. 댓글 추이', markers=True)
    fig4.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig4, width="stretch", height=280)

with col5:
    fig5 = px.line(df, x='date', y='average_view_duration', title='5. 평균 시청 시간(초)', markers=True)
    fig5.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig5, width="stretch", height=280)

with col6:
    fig6 = px.line(df, x='date', y='average_view_percentage', title='6. 평균 시청 유지율(%)', markers=True)
    fig6.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig6, width="stretch", height=280)

# ===================== 하단 테이블 =====================
st.subheader(f"📋 {selected_month} 상세 데이터")

df_korean = df.rename(columns={
    'date': '날짜',
    'views': '조회수',
    'subscribers_gained': '구독자 증가',
    'likes': '좋아요',
    'comments': '댓글',
    'average_view_duration': '평균 시청 시간(초)',
    'average_view_percentage': '평균 시청 유지율(%)'
})

df_korean['날짜'] = df_korean['날짜'].dt.date   # 이제 정상 동작

st.dataframe(df_korean, width="stretch", hide_index=True)