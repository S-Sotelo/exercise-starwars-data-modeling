import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    favorites_characters = relationship('FavoriteCharacter', back_populates='user', cascade="all, delete-orphan")
    favorites_planets = relationship('FavoritePlanet', back_populates='user', cascade="all, delete-orphan")

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    
    user = relationship('User', back_populates='favorites_characters')
    character = relationship('Character', back_populates='favorites_characters')

class Character(Base):
    __tablename__ = 'characters'  
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    gender = Column(String(50), nullable=False)
    created = Column(DateTime, nullable=False)
    url = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    favorites_characters = relationship('FavoriteCharacter', back_populates='character')

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    
    user = relationship('User', back_populates='favorites_planets')
    planet = relationship('Planet', back_populates='favorites_planets')

class Planet(Base):
    __tablename__ = 'planets' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    favorites_planets = relationship('FavoritePlanet', back_populates='planet')

## Draw from SQLAlchemy base
try:
    render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
