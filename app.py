import streamlit as st
import pandas as pd
from src.loader import carregar_dados
import src.charts as ch
st.set_page_config(layout='wide', page_title="Painel SDR", page_icon="📈")
st.title("Painel SDR – Reuniões")

df = carregar_dados()

# Métricas simuladas (substitua por cálculo real)
meta_dia = 30
meta_semana = 165
realizado_dia = df[df['data_reuniao'].dt.date == pd.Timestamp.today().date()].shape[0]
realizado_semana = df[df['data_reuniao'] >= pd.Timestamp.today() - pd.Timedelta(days=7)].shape[0]

# Linha 1 – Velocímetros
col1, col2 = st.columns(2)
with col1:
    ch.velocimetro_simples("Meta do Dia", realizado_dia, meta_dia)
with col2:
    ch.velocimetro_simples("Meta da Semana", realizado_semana, meta_semana)

# Linha 2 – Linha + Barras
col3, col4 = st.columns(2)
with col3:
    ch.grafico_linha_reunioes_diarias(df)
with col4:
    ch.grafico_barras_pre_venda(df)
