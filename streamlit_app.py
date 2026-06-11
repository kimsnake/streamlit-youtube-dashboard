import streamlit as st
import pandas as pd
import plotly.express as px

# ===================== 페이지 설정 =====================
st.set_page_config(
    page_title="NightFocus Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== Custom CSS (Purple Theme + Spacing) =====================
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background-color: #F8F5FF;
    }
    
    /* 메인 컨테이너 여백 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* 제목 스타일 */
    h1 {
        color: #4F46E5;
        margin-bottom: 0.5rem;
    }
    
    /* 서브헤더 스타일 */
    h2, h3 {
        color: #4338CA;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    /* Selectbox 스타일 */
    .stSelectbox > div > div {
        background-color: white;
        border: 1px solid #C4B5FD;
        border-radius: 8px;
    }
    
    /* 데이터프레임 스타일 */
    .stDataFrame {
        border: 1px solid #C4B5FD;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .stDataFrame thead tr th {
        background-color: #7C3AED !important;
        color: white !important;
        font-weight: 600;
    }
    
    /* 차트 컨테이너 여백 */
    .stPlotlyChart {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def style_plotly_chart(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",      # 차트 전체 배경 투명
        plot_bgcolor="rgba(0,0,0,0)",       # 그래프 영역 배경 투명
        font=dict(color="#374151"),
        margin=dict(l=40, r=20, t=40, b=30),
        hoverlabel=dict(
            bgcolor="#7C3AED",
            font_size=12,
            font_color="white"
        )
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="#E0E7FF",
        linecolor="#C4B5FD"
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#E0E7FF",
        linecolor="#C4B5FD"
    )
    return fig

# ===================== 제목 + 채널 링크 =====================
st.markdown(
    """
    <h1>
        🎵 <a href="https://www.youtube.com/@NightFocusAudio_1H" target="_blank" style="text-decoration: none; color: inherit;">
        NightFocus Dashboard
        </a>
    </h1>
    <p style="color: #6B7280; font-size: 1.05rem; margin-bottom: 1.5rem;">
        YouTube 채널 데이터를 자동으로 수집하여 시각화한 대시보드입니다.
    </p>
    """,
    unsafe_allow_html=True
)


conn = st.connection("neon", type="sql")


# ===================== 월 선택 =====================
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


# ===================== 데이터 조회 =====================
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

df['date'] = pd.to_datetime(df['date'])


# ===================== 그래프 영역 =====================
st.subheader(f"📈 {selected_month} 채널 자동 수집 데이터 추이")

# 1행
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    fig1 = px.line(df, x='date', y='views', title='1. 조회수 추이', markers=True)
    fig1 = style_plotly_chart(fig1)
    fig1.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig1, width="stretch", height=280)

with col2:
    fig2 = px.line(df, x='date', y='subscribers_gained', title='2. 구독자 증가 추이', markers=True)
    fig2 = style_plotly_chart(fig2)
    fig2.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig2, width="stretch", height=280)

with col3:
    fig3 = px.line(df, x='date', y='likes', title='3. 좋아요 추이', markers=True)
    fig3 = style_plotly_chart(fig3)
    fig3.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig3, width="stretch", height=280)

# 2행
col4, col5, col6 = st.columns(3, gap="large")

with col4:
    fig4 = px.line(df, x='date', y='comments', title='4. 댓글 추이', markers=True)
    fig4 = style_plotly_chart(fig4)
    fig4.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig4, width="stretch", height=280)

with col5:
    fig5 = px.line(df, x='date', y='average_view_duration', title='5. 평균 시청 시간(초)', markers=True)
    fig5 = style_plotly_chart(fig5)
    fig5.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig5, width="stretch", height=280)

with col6:
    fig6 = px.line(df, x='date', y='average_view_percentage', title='6. 평균 시청 유지율(%)', markers=True)
    fig6 = style_plotly_chart(fig6)
    fig6.update_xaxes(tickformat="%m-%d", nticks=6)
    st.plotly_chart(fig6, width="stretch", height=280)


# ===================== 테이블 영역 =====================
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

df_korean['날짜'] = df_korean['날짜'].dt.date

st.dataframe(df_korean, width="stretch", hide_index=True)