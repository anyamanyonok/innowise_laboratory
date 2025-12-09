from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base

# SQLite база данных (файл book_collection.db в той же папке)
SQLALCHEMY_DATABASE_URL = "sqlite:///./book_collection.db"

# Создаем движок для подключения к БД
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Нужно только для SQLite
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для создания таблиц
def create_tables():
    Base.metadata.create_all(bind=engine)

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()