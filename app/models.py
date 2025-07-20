from sqlalchemy import Column, String, Integer, Float, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid
import enum
from datetime import datetime

Base = declarative_base()

class FuelType(enum.Enum):
    GASOLINA = "Gasolina"
    DIESEL = "Diesel"
    FLEX = "Flex"
    ELETRICO = "Elétrico"
    HIBRIDO = "Híbrido"

class TransmissionType(enum.Enum):
    MANUAL = "Manual"
    AUTOMATICO = "Automático"

class Car(Base):
    __tablename__ = "cars"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    motorizacao = Column(String, nullable=False)
    tipo_combustivel = Column(Enum(FuelType), nullable=False)
    cor = Column(String, nullable=False)
    quilometragem = Column(Integer, nullable=False)
    numero_portas = Column(Integer, nullable=False)
    transmissao = Column(Enum(TransmissionType), nullable=False)
    preco = Column(Float, nullable=False)
    placa = Column(String, nullable=False, unique=True)
    data_cadastro = Column(DateTime, default=datetime.now())
