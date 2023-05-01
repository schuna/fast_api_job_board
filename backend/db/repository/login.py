from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.users import User


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user
