from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from app import models, schemas
from app.hashing import Hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hash.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, hashed_password=hashed_password, username=user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str) -> schemas.User:
    stmt = select(models.User).where(models.User.username == username)
    result = db.execute(stmt).first()
    if result is None:
        return None
    user = schemas.UserAuthenticate.from_orm(result.User)
    return user
