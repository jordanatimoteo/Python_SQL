from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import INT, Time

Base = declarative_base()



class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    nome = Column(String(25))
    data_nascimento = Column(Date)
    def __repr__(self):
        return f'Usuario {self.nome}'
    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    __tablename__ = 'atividade'
    id_atividade = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    dia = Column(Date, unique=True, nullable=False)
    hora = Column(Time, nullable=False)
    quilometros = Column(Integer,unique=True, nullable=False)
    tipo = Column(String(255), unique=True, nullable=False)
    local = Column(String(255), unique=True, nullable=False)



class Curtida(Base):
    __tablename__ = 'curtida'
    id_curtida =  Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_atividade = Column(Integer, ForeignKey('atividade.id_atividade'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref="Curtida")
    atividade = relationship("Atividade", backref="Curtida")

class Comentario(Base):
    __tablename__ = 'comentario'
    id_comentario = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_atividade = Column(Integer, ForeignKey('atividade.id_atividade'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    comentario = Column(String(255), unique=True, nullable=False)
    usuario = relationship("Usuario", backref="Comentario")
    atividade = relationship("Atividade", backref="Comentario")

class Curtida_comentario(Base):
    __tablename__ = 'curtida_comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_comentario = Column(Integer, ForeignKey('comentario.id_comentario'))
    usuario = relationship("Usuario", backref=" Curtida_comentario")
    comentario = relationship("Comentario", backref=" Curtida_comentario")