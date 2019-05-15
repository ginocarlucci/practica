from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey,create_engine
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()


class Persona(Base):
    __tablename__ = 'persona'
    idPersona = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String)
    fechaNacimiento = Column(DateTime)
    DNI = Column(Integer)
    altura = Column(Integer)
    pesos = relationship("PersonaPeso",back_populates="persona")

class PersonaPeso(Base):
    __tablename__ = 'personaPeso'
    idPeso = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    peso = Column(Integer)
    idPersona = Column(Integer,ForeignKey('persona.idPersona'))
    persona = relationship(Persona,back_populates="pesos")



engine = create_engine('sqlite://')
Base.metadata.bind = engine
# ---- creamos una sesión para admin datos
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
