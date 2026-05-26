from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(String(60))
    avatar: Mapped[Optional[str]] = mapped_column(String(255))
    subscription_date: Mapped[int] = mapped_column(Integer, nullable=False)

    favorito: Mapped[List["Favoritos"]] = relationship(back_populates="usuario")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "avatar": self.avatar,
            "subscription_date": self.subscription_date
        }


class Planetas(db.Model):
    __tablename__ = "planeta"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(100), nullable=False)
    land: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[Optional[int]] = mapped_column(Integer)

    favorito: Mapped[List["Favoritos"]] = relationship(back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "land": self.land,
            "population": self.population
        }


class Personajes(db.Model):
    __tablename__ = "personaje"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    height: Mapped[Optional[int]] = mapped_column(Integer)
    weight: Mapped[Optional[int]] = mapped_column(Integer)

    favorito: Mapped[List["Favoritos"]] = relationship(back_populates="personaje")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight
        }


class Naves(db.Model):
    __tablename__ = "nave"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    speed: Mapped[Optional[int]] = mapped_column(Integer)
    
    favorito: Mapped[List["Favoritos"]] = relationship(back_populates="nave")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "speed": self.speed
        }


class Favoritos(db.Model):
    __tablename__ = "favorito"

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    personaje_id: Mapped[Optional[int]] = mapped_column(ForeignKey("personaje.id"))
    planeta_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planeta.id"))
    nave_id: Mapped[Optional[int]] = mapped_column(ForeignKey("nave.id"))

    usuario: Mapped["Usuario"] = relationship(back_populates="favorito")
    personaje: Mapped[Optional["Personajes"]] = relationship(back_populates="favorito")
    planeta: Mapped[Optional["Planetas"]] = relationship(back_populates="favorito")
    nave: Mapped[Optional["Naves"]] = relationship(back_populates="favorito")

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "nave_id": self.nave_id
        }
