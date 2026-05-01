import pytest
from models import Subject

def test_add_subject(db_session):
    """Тест на добавление предмета."""
    new_subject = Subject(name="Математика", code="MATH101")
    db_session.add(new_subject)
    db_session.commit()

    # Проверяем, что запись есть в БД
    result = db_session.query(Subject).filter_by(code="MATH101").first()
    assert result is not None
    assert result.name == "Математика"

def test_update_subject(db_session):
    """Тест на изменение предмета."""
    subject = Subject(name="Физика", code="PHYS202")
    db_session.add(subject)
    db_session.commit()

    # Меняем название
    subject.name = "Астрофизика"
    db_session.commit()

    updated = db_session.query(Subject).get(subject.id)
    assert updated.name == "Астрофизика"

def test_delete_subject(db_session):
    """Тест на удаление предмета."""
    subject = Subject(name="Химия", code="CHEM303")
    db_session.add(subject)
    db_session.commit()

    # Удаляем запись
    db_session.delete(subject)
    db_session.commit()

    deleted = db_session.query(Subject).get(subject.id)
    assert deleted is None