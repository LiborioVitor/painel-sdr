import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def grafico_reunioes_acumuladas(df):
    # Agrupar por dia
    df_dia = df.groupby(df['data_reuniao'].dt.date).size().reset_index(name='quantidade')
    df_dia = df_dia.sort_values('data_reuniao')

    # Acumulado real
    df_dia['acumulado'] = df_dia['quantidade'].cumsum()
    df_dia['acumulado_formatado'] = df_dia['acumulado'].astype(str)

    # Datas para meta
    datas = pd.date_range(start=df_dia['data_reuniao'].min(), end=df_dia['data_reuniao'].max())
    df_meta = pd.DataFrame({'data_reuniao': datas})
    df_meta['meta'] = [(i + 1) * 25 for i in range(len(df_meta))]  # 25 reuniões por dia

    # Gráfico de barras (acumulado real)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_dia['data_reuniao'],
        y=df_dia['acumulado'],
        name='Reuniões Acumuladas',
        text=df_dia['acumulado_formatado'],
        textposition='outside',
        marker_color='#2813AD'
    ))

    # Linha da meta
    fig.add_trace(go.Scatter(
        x=df_meta['data_reuniao'],
        y=df_meta['meta'],
        mode='lines+markers',
        name='Meta Acumulada',
        line=dict(color='#F7B304', width=3, dash='solid'),
        marker=dict(size=6)
    ))

    # Layout
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#000000', size=16),
        title=dict(text='Reuniões Acumuladas por Dia (Mês Atual)', x=0.5, font=dict(size=22)),
        margin=dict(t=70, b=40),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_xaxes(
        tickvals=df_dia['data_reuniao'],
        ticktext=pd.to_datetime(df_dia['data_reuniao']).dt.strftime('%d/%m'),
        title='Data',
        tickfont=dict(size=14)
    )
    fig.update_yaxes(title='Total Acumulado', tickfont=dict(size=14))

    return fig

def grafico_reunioes_por_agente(df):
    df_agente = df.groupby(['sub_equipe', 'pre_venda']).size().reset_index(name='quantidade')
    df_agente = df_agente.sort_values(by='quantidade', ascending=True)

    fig = px.bar(
        df_agente,
        x='quantidade',
        y='pre_venda',
        color='sub_equipe',
        orientation='h',
        title='Reuniões por Agente (mês atual)',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#000000', size=14),
        title=dict(x=0.5, font=dict(size=20)),
        legend_title='Time',
        margin=dict(t=60, b=40)
    )
    return fig

def grafico_pizza_reunioes_por_time(df):
    df_time = df['sub_equipe'].value_counts().reset_index()
    df_time.columns = ['sub_equipe', 'quantidade']

    fig = px.pie(
        df_time,
        names='sub_equipe',
        values='quantidade',
        title='Distribuição de Reuniões por Time',
        color_discrete_sequence=px.colors.sequential.Sunset
    )
    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(color='#000000', size=14),
        title=dict(x=0.5, font=dict(size=20)),
        showlegend=True
    )
    return fig
