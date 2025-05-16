import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

from src.loader import carregar_reunioes_mes_atual, carregar_reunioes_por_time
from src.charts import grafico_reunioes_acumuladas, grafico_reunioes_por_agente, grafico_pizza_reunioes_por_time

# Configuração da página
st.set_page_config(layout='wide', page_title="Painel de Reuniões", page_icon="📅")

# Autoatualização a cada 30 segundos
st_autorefresh(interval=30 * 1000, key="refresh")

# Controle de páginas
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 0
st.session_state.pagina_atual = (st.session_state.pagina_atual + 1) % 2

# Estilo visual customizado
st.markdown("""
    <style>
        html, body, .main, .block-container, .stApp {
            background-color: #0E0E0E !important;
            color: #FFFFFF !important;
        }
        .block-container {
            padding-top: 0.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        h1 {
            color: #F7B304 !important;
            font-size: 2.2em !important;
            text-align: center;
            margin-bottom: 0.2rem !important;
            margin-top: 0 !important;
        }
        h6 {
            text-align: center;
            color: #AAAAAA !important;
            font-size: 1em !important;
            margin-top: 0 !important;
        }
        .stMarkdown, .stText, .stPlotlyChart {
            font-size: 1.2em !important;
        }
        .js-plotly-plot .plotly .modebar {
            display: none !important;
        }
        #MainMenu, footer, header {
            visibility: hidden;
        }
        .viewerBadge_container__1QSob {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown(f"""
    <h1>📅 Painel de Reuniões SDR</h1>
    <h6>Atualizado em: {(datetime.now() - timedelta(hours=3)).strftime('%d/%m/%Y %H:%M:%S')}</h6>
""", unsafe_allow_html=True)

# Página 1: Reuniões acumuladas
if st.session_state.pagina_atual == 0:
    df = carregar_reunioes_mes_atual()
    fig = grafico_reunioes_acumuladas(df)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# Página 2: Por time e agente
else:
    df = carregar_reunioes_por_time()
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_reunioes_por_agente(df), use_container_width=True, config={"displayModeBar": False})
    with col2:
        st.plotly_chart(grafico_pizza_reunioes_por_time(df), use_container_width=True, config={"displayModeBar": False})
