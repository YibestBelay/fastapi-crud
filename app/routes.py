from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    created = crud.create_book(db=db, book=book)
    if created is None:
        raise HTTPException(status_code=400, detail="Book with this title already exists")
    return created


@router.get("/books/", response_model=list[schemas.BookResponse])
def read_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)


@router.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/books/{book_id}", response_model=schemas.BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if updated is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

