from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CarBase(BaseModel):
    marca: str
    modelo: str
    ano: int
    motorizacao: str
    tipo_combustivel: str
    cor: str
    quilometragem: int
    numero_portas: int
    transmissao: str
    preco: float
    placa: str

class CarCreate(CarBase):
    pass

class CarOut(CarBase):
    id: str
    data_cadastro: datetime

    model_config = ConfigDict(from_attributes=True)

class CarFilter(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    tipo_combustivel: Optional[str] = None
    cor: Optional[str] = None
    transmissao: Optional[str] = None
    preco_min: Optional[float] = None
    preco_max: Optional[float] = None
