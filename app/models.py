from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id:int
    title:str
    author:str
    description: Optional[str] = None
    rating: float= Field(..., ge=0, le=5)

