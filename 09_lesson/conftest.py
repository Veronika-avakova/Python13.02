import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Убедитесь, что вы импортируете Base из models

# Используем вашу строку подключения
db_connection_string = "postgresql://postgres@localhost:5432/postgres"
engine = create_engine(db_connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    # Создаём таблицы перед тестом
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    try:
        yield session
    finally:
        # Удаляем данные из таблиц и сами таблицы после теста
        session.rollback()  # Откатываем любые незавершённые транзакции

        # Используем сессию для удаления данных
        for tbl in reversed(Base.metadata.sorted_tables):
            session.execute(tbl.delete())

        session.commit()  # Фиксируем изменения (удаление строк)

        # Удаляем таблицы
        Base.metadata.drop_all(bind=engine)

        session.close()