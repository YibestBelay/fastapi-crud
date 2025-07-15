from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    rating: int = Field(..., le=5) 


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
