# Querys e carregamento dos dados para DataFrames

from sqlalchemy import text
import pandas as pd
from src.db import get_engine


def carregar_reunioes_mes_atual():
    engine = get_engine()
    query = text("""
        SELECT STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y') AS data_reuniao
        FROM aux_comercial_agendamentos.reunioes_sdrs_geral rsg 
        LEFT JOIN comportamento.equipes e ON rsg.pre_venda = e.username
        WHERE YEAR(STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y')) = YEAR(CURDATE())
          AND MONTH(STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y')) = MONTH(CURDATE())
          AND reuniao_ocorrida = 1
          AND e.sub_equipe in ('SDR','BDR')
    """)
    df = pd.read_sql(query, con=engine)
    engine.dispose()
    df['data_reuniao'] = pd.to_datetime(df['data_reuniao'])
    return df

def carregar_reunioes_por_time():
    engine = get_engine()
    query = text("""
        SELECT e.sub_equipe, rsg.pre_venda
        FROM aux_comercial_agendamentos.reunioes_sdrs_geral rsg 
        LEFT JOIN comportamento.equipes e ON rsg.pre_venda = e.username
        WHERE YEAR(STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y')) = YEAR(CURDATE())
          AND MONTH(STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y')) = MONTH(CURDATE())
          AND reuniao_ocorrida = 1
          AND e.sub_equipe in ('SDR','BDR')
    """)
    df = pd.read_sql(query, con=engine)
    engine.dispose()
    return df