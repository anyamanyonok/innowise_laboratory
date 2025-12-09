from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import os

import models
import schemas
from database import engine, get_db, create_tables

# Явно создаем таблицы при запуске
print("Создание таблиц в базе данных...")
create_tables()
print("Таблицы созданы успешно!")

# Проверяем существование файла БД
db_file = "book_collection.db"
if os.path.exists(db_file):
    print(f"Файл базы данных найден: {db_file}")
else:
    print(f"Файл базы данных будет создан при первом запросе")

app = FastAPI(
    title="Book Collection API",
    description="API для управления коллекцией книг",
    version="1.0.0"
)


# POST /books/ - Добавить новую книгу
@app.post("/books/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Добавить новую книгу в коллекцию
    """
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# GET /books/ - Получить все книги
@app.get("/books/", response_model=List[schemas.BookResponse])
def get_all_books(
        skip: int = Query(0, ge=0, description="Количество записей для пропуска"),
        limit: int = Query(100, ge=1, le=100, description="Количество записей на странице"),
        db: Session = Depends(get_db)
):
    """
    Получить список всех книг с поддержкой пагинации
    """
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books


# GET /books/{book_id} - Получить книгу по ID
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    """
    Получить информацию о конкретной книге по её ID
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


# PUT /books/{book_id} - Обновить книгу
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
        book_id: int,
        book_update: schemas.BookUpdate,
        db: Session = Depends(get_db)
):
    """
    Обновить информацию о книге
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    # Обновляем только переданные поля
    update_data = book_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book


# DELETE /books/{book_id} - Удалить книгу
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Удалить книгу из коллекции
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    db.delete(book)
    db.commit()
    return


# GET /books/search/ - Поиск книг
@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
        title: Optional[str] = Query(None, description="Поиск по названию"),
        author: Optional[str] = Query(None, description="Поиск по автору"),
        year: Optional[int] = Query(None, description="Поиск по году"),
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=100),
        db: Session = Depends(get_db)
):
    """
    Поиск книг по различным критериям
    """
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.contains(title))
    if author:
        query = query.filter(models.Book.author.contains(author))
    if year:
        query = query.filter(models.Book.year == year)

    books = query.offset(skip).limit(limit).all()
    return books


# Корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в API коллекции книг!"}