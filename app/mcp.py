from .schemas import CarFilter
from fastapi import HTTPException

def parse_mcp_payload(payload: dict) -> CarFilter:
    try:
        return CarFilter(**payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro no payload MCP: {e}")
