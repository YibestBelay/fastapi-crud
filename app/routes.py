from fastapi import APIRouter,HTTPException
from typing import List
from .db import books_db
from .models import Book

router = APIRouter()

@router.get('/')
def read_root():
    return{"message":"Hello, Welcome to my crud Op"}

@router.get('/books/',response_model=List[Book])
def get_books():
    return books_db

@router.post('/books/bulk',response_model=List[Book])
def create_book(new_books:List[Book]):
    for book in new_books:
         if any(b.id == book.id for b in books_db):
                raise HTTPException(status_code=400, detail=f'book with id {book.id} already exist')
    books_db.extend(new_books)
    return new_books

@router.post('/books/',response_model=Book)
def create_book(book:Book):
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail=f'book with id {book.id} already exist')
    books_db.append(book)
    return book

@router.get('/books/{book_id}',response_model=Book)
def get_book(book_id:int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code='404',detail='Book not found')    

@router.put('/books/{book_id}',response_model=Book)
def update_book(book_id:int , updated_book: Book):
    for index,book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code='404',detail='Book not found') 

@router.delete('/books/{book_id}')
def delete_book(book_id:int ):
    for index,book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index] 
            return {"message": f"Book with Title {book.title} has been deleted"}
    raise HTTPException(status_code='404',detail='Book not found')