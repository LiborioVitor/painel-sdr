import plotly.graph_objects as go
import streamlit as st
import altair as alt
from datetime import datetime, timedelta


def grafico_velocimetro(titulo, valor, meta):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=valor,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': titulo},
        gauge={
            'axis': {'range': [None, meta]},
            'bar': {'color': "royalblue"},
            'steps': [
                {'range': [0, meta * 0.5], 'color': "lightgray"},
                {'range': [meta * 0.5, meta], 'color': "gray"},
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

def velocimetro_simples(titulo, valor, meta):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=valor,
        title={'text': f"{titulo}"},
        gauge={
            'axis': {'range': [0, meta]},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "lightgray",
            'shape': "angular"
        }
    ))
    fig.update_layout(height=250, margin=dict(t=40, b=20, l=20, r=20))
    st.plotly_chart(fig, use_container_width=True)

def velocimetro_horizontal(titulo, valor, meta):
    fig = go.Figure(go.Indicator(
        mode="number+gauge",
        value=valor,
        title={'text': f"{titulo}"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [None, meta]},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "lightgray"
        }
    ))
    fig.update_layout(height=120, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig, use_container_width=True)

def grafico_linha_reunioes_diarias(df):
    df_agg = df.groupby(df['data_reuniao'].dt.date).size().reset_index(name='qtd')
    df_agg = df_agg.sort_values('data_reuniao').tail(10)

    chart = alt.Chart(df_agg).mark_line(point=True).encode(
        x=alt.X('data_reuniao:T', title='Data'),
        y=alt.Y('qtd:Q', title='Reuniões'),
        tooltip=['data_reuniao', 'qtd']
    ).properties(
        width=600,
        height=300,
        title="Reuniões nos Últimos 10 Dias"
    )
    st.altair_chart(chart, use_container_width=True)

def grafico_barras_pre_venda(df):
    limite_data = datetime.now() - timedelta(days=30)
    df_30 = df[df['data_reuniao'] >= limite_data]
    contagem = df_30['pre_venda'].value_counts().reset_index()
    contagem.columns = ['pre_venda', 'quantidade']

    chart = alt.Chart(contagem).mark_bar().encode(
        x=alt.X('quantidade:Q', title='Nº de Reuniões'),
        y=alt.Y('pre_venda:N', sort='-x', title='Pré-vendedor'),
        tooltip=['pre_venda', 'quantidade']
    ).properties(
        width=600,
        height=300,
        title="Reuniões por Pré-vendedor (últimos 30 dias)"
    )
    st.altair_chart(chart, use_container_width=True)
