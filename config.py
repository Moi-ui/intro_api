import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wcc@2023")
    SQLALCHEMY_DATABASE_UML = os.getenv("DATABASE", "postegresql://postgres:SECRET_KEY@127.0.0.1:5433/tarefas_3b")
    #Com isso na hora de instanciar o aplicativo na instancia do FlaskSQLALchemy não será mostrado.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    