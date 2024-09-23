from fastapi import  HTTPException, Query
from pydantic import BaseModel



class QueryResponse(BaseModel):
    title: str
    content: str
    relevance: float
