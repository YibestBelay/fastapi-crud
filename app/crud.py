from sqlalchemy.orm import Session
from . import models, schemas


def create_book(db: Session, book: schemas.BookCreate):
    existing_book = db.query(models.Book).filter(models.Book.title == book.title).first()
    if existing_book:
        return None
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book


def update_book(db: Session, book_id: int, updated_data: schemas.BookCreate):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    for key, value in updated_data.dict().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

