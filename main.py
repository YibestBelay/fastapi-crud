from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional,Union

app=FastAPI()

class Book(BaseModel):
    id:int
    title:str
    author:str
    description: Optional[str] = None
    rating: float

books_db:List[Book] = []


@app.get('/')
def read_root():
    return{"message":"Hello, Welcome to my crud Op"}

@app.get('/books/',response_model=List[Book])
def get_books():
    return books_db

@app.post('/books/bulk',response_model=Book)
def create_book(new_books:List[Book]):
    books_db.extend(new_books)
    return new_books

@app.get('/books/{book_id}',response_model=Book)
def get_book(book_id:int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code='404',detail='Book not found')    

@app.put('/books/{book_id}',response_model=Book)
def update_book(book_id:int , updated_book: Book):
    for index,book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code='404',detail='Book not found') 

@app.delete('/books/{book_id}')
def delete_book(book_id:int ):
    for index,book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index] 
            return {"message": f"Book with Title {book.title} has been deleted"}
    raise HTTPException(status_code='404',detail='Book not found')

