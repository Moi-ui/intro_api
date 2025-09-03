import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wcc@2023")
    password = os.getenv("DATABASE_PASSWORD", "wcc@2023")
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"postgresql://postgres:{encoded_password}@127.0.0.1:5432/tarefas_3b")
    
    
    #comentar a linha abaixo
    # SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SECRET_KEY@127.0.0.1:5432/tarefas_3b")
    
    #ESSA LINHA NÃO COMENTA!
    #Com isso na hora de instanciar o aplicativo na instancia do FlaskSQLALchemy não será mostrado.
    SQLALCHEMY_TRACK_MODIFICATIONS = False