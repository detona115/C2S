from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from .database import SessionLocal, init_db
from .schemas import CarOut, CarFilter
from .crud import get_cars
from .mcp import parse_mcp_payload
from typing import List


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="API de Veículos via MCP", lifespan=lifespan)

@app.post("/mcp/query", response_model=List[CarOut])
def mcp_query(payload: dict, db: Session = Depends(get_db)):
    filters = parse_mcp_payload(payload)
    cars = get_cars(db, filters)
    return cars
