# Conexão com o banco de dados via SQLAlchemy

from sqlalchemy import create_engine
from config.db_config import DB_CONFIG

def get_engine():
    return create_engine(
        f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    )
