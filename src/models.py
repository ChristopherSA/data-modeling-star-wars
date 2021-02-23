import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planetas_props(Base):
    __tablename__ = 'Planetas_props'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey('Planetas.id'))
    name = Column(String(250), nullable=False)
    clima = Column(String(250))
    diametro = Column(String(250))
    gravedad = Column(String(250))
    nombre = Column(String(250))
    periodo_orbital = Column(String(250))
    poblacion = Column(String(250))
    habitantes = Column(String(250))
    periodo_rotacion = Column(String(250))
    superficie_acuatica = Column(String(250))
    terreno = Column(String(250))
    def to_dict(self):
        return{}

class Planetas(Base):
    __tablename__ = 'Planetas'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Url = Column(String(250))
    Planetas = relationship(Planetas_props)
    def to_dict(self):
        return{}


class Personajes_props(Base):
    __tablename__ = 'Personajes_props'
    personaje_id = Column(Integer, ForeignKey('Personajes.id'))
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    altura = Column(String(250))
    masa = Column(String(250))
    pelo = Column(String(250))
    piel = Column(String(250))
    ojos = Column(String(250))
    cumpleaños = Column(String(250))
    genero = Column(String(250))
    creacion = Column(String(250))
    editado = Column(String(250))
    nombre = Column(String(250))
    mundo_origen = Column(String(250))
    def to_dict(self):
        return{}

class Personajes(Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('Personaje.id'))
    Personaje = relationship(Personajes_props)
    def to_dict(self):
        return{}

class Favoritos(Base):
    __tablename__ = 'Favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    personajes_id = Column(Integer, ForeignKey('Personajes.id'))
    planetas_id = Column(Integer, ForeignKey('Planetas.id'))
    Personajes = relationship(Personajes_props)
    Planetas = relationship(Planetas_props)
    def to_dict(self):
        return{}

class Usuarios(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(250), nullable=False)
    apellido_1 = Column(String(250), nullable=False)
    apellido_2 = Column(String(250), nullable=False)
    id_usuario = Column(Integer, primary_key=True)
    contraseña = Column(String(250), nullable=False)
    Favoritos = relationship(Favoritos)
    def to_dict(self):
        return{}

render_er(Base, 'diagram.png')