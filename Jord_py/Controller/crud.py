from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker


from model.models import Usuario, Atividade

engine = create_engine(
    "mysql+pymysql://root:@localhost/python_5?charset=utf8mb4", echo=True)


Session = sessionmaker(bind=engine)
session = Session()


def read():
    tuplas = session.query(Usuario).order_by(Usuario.id)
    for tupla in tuplas:
        print(tupla.id, " - ", tupla.email)

    for email, nome in session.query(Usuario.email, Usuario.nome):
        print(email, '-' ,  nome)

def calcula():
    tuplas = session.query(Atividade).order_by(Atividade.quilometros)
    for tupla in tuplas:
        print(tupla.quilometros)
