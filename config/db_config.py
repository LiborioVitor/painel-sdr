import os
import streamlit as st

if "DB_USER" in st.secrets:
    # Produção (Streamlit Cloud)
    DB_CONFIG = {
        "user": st.secrets["DB_USER"],
        "password": st.secrets["DB_PASSWORD"],
        "host": st.secrets["DB_HOST"],
        "database": st.secrets["DB_NAME"]
    }
else:
    # Desenvolvimento local (.env)
    from dotenv import load_dotenv
    load_dotenv()
    DB_CONFIG = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME")
    }
