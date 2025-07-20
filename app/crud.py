from sqlalchemy.orm import Session
from .models import Car
from .schemas import CarCreate, CarFilter

def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_cars(db: Session, filters: CarFilter):
    query = db.query(Car)
    if filters.marca:
        query = query.filter(Car.marca == filters.marca)
    if filters.modelo:
        query = query.filter(Car.modelo == filters.modelo)
    if filters.ano:
        query = query.filter(Car.ano == filters.ano)
    if filters.tipo_combustivel:
        query = query.filter(Car.tipo_combustivel == filters.tipo_combustivel)
    if filters.cor:
        query = query.filter(Car.cor == filters.cor)
    if filters.transmissao:
        query = query.filter(Car.transmissao == filters.transmissao)
    if filters.preco_min is not None:
        query = query.filter(Car.preco >= filters.preco_min)
    if filters.preco_max is not None:
        query = query.filter(Car.preco <= filters.preco_max)
    return query.all()
