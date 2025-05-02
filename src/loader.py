# Querys e carregamento dos dados para DataFrames

from sqlalchemy import text
import pandas as pd
from src.db import get_engine

def carregar_dados():
    engine = get_engine()
    query = text("""
        SELECT oportunidade, 
               pre_venda,
               vendedor,
               STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y') AS data_reuniao
        FROM aux_comercial_agendamentos.reunioes_sdrs_geral rsg 
        LEFT JOIN comportamento.equipes e ON rsg.pre_venda = e.username
        WHERE year(STR_TO_DATE(data_reuniao_calculada, '%d/%m/%Y')) >= 2025
          AND reuniao_ocorrida = 1
          AND e.sub_equipe = 'SDR'
    """)

    df = pd.read_sql(query, con=engine)
    df['data_reuniao'] = pd.to_datetime(df['data_reuniao'])
    
    return df

