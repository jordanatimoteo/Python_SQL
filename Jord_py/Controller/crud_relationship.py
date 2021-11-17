from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from crud import calcula, read

from model.models import Comentario, Curtida, Curtida_comentario, Usuario, Atividade

engine = create_engine(
    "mysql+pymysql://root:@localhost/python_5", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    user1 = Usuario(email='herbertrarsch@gmail.com', senha='123', nome='Mestre do Python.', data_nascimento='2003-03-03')
    session.add(user1)
    session.commit()
    atividade1 = Atividade(dia='2021-09-09',hora='09:30:00',quilometros='10',tipo='Corrida Maluca', local='CEFET-MG')
    session.add(atividade1)
    session.commit()
def create2():
    user2 = Usuario(email='juanmarques@gmail.com', senha='1233543', nome='Cabeleira.', data_nascimento='2003-01-01')
    session.add(user2)
    session.commit()
    atividade1 = Atividade(dia='2021-08-08',hora='09:30:00',quilometros='30',tipo='Basquete Fantasia', local='Centro de Varginha')
    session.add(atividade1)
    session.commit()
def create3():
    user3 = Usuario(email='danilochagas@gmail.com', senha='12345678', nome='Indio Neon.', data_nascimento='2003-02-02')
    session.add(user3)
    session.commit()
    atividade1 = Atividade(dia='2021-07-07',hora='07:30:00',quilometros='1000',tipo='Maratona de fugir de onça', local='Amazônia')
    session.add(atividade1)
    session.commit()

def curtir():
    curtida1 = Curtida(id_atividade='3', usuario_id='1')
    session.add(curtida1)
    session.commit()
    curtida2 = Curtida(id_atividade='2',usuario_id='2')
    session.add(curtida2)
    session.commit()
    curtida3 = Curtida(id_atividade='1',usuario_id='3')
    session.add(curtida3)
    session.commit()
def Comentar():
    comentario1 = Comentario(id_atividade='3',usuario_id='1',comentario='Legal')
    session.add(comentario1)
    session.commit()
    comentario2 = Comentario(id_atividade='2',usuario_id='3',comentario='muito legal')
    session.add(comentario2)
    session.commit()
    comentario3 = Comentario(id_atividade='1',usuario_id='2',comentario='Dahoras')
    session.add(comentario3)
    session.commit() 

def Curtir_comentar():
    curtida1 = Curtida_comentario(id_usuario='1',id_comentario='3')
    session.add(curtida1)
    session.commit() 
    curtida2 = Curtida_comentario(id_usuario='3',id_comentario='2')
    session.add(curtida2)
    session.commit() 
    curtida3 = Curtida_comentario(id_usuario='2',id_comentario='1')
    session.add(curtida1)
    session.commit() 
    

create1()
create2()
create3()
curtir()
Comentar()
Curtir_comentar()
read()
calcula()
