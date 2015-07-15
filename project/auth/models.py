from sqlalchemy import Column, Integer, String
from project.database import Base, db_session
from werkzeug.security import generate_password_hash
from enum import IntEnum

from project.lib.orm.types import TypeEnum


class User(Base):
    __tablename__ = 'users'

    #  noinspection PyTypeChecker
    ROLE = IntEnum('Role', {
        'staff': 0,
        'superuser': 1,
    })

    id = Column(Integer, primary_key=True)
    login = Column(String(30), unique=True)
    password = Column(String(100))
    name = Column(String(30))
    surname = Column(String(30))
    email = Column(String(30))
    role = Column(TypeEnum(ROLE), default=ROLE.staff)

    def __init__(self, login, password, email, name=None,
                 surname=None):
        self.email = email
        self.login = login
        self.name = name
        self.surname = surname
        self.set_password(password)

    def __repr__(self):
        return '<User {}>'.format(self.get_full_name())

    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def is_superuser(self):
        return self.role == self.ROLE.superuser

    def set_password(self, password):
        self.password = generate_password_hash(password)

    @staticmethod
    def authenticate(login, password):
        from project.bl.auth import authenticate as bl_authenticate
        return bl_authenticate(login, password)

    @staticmethod
    def create_superuser(login, password):
        from project.bl.auth import create_superuser as bl_create_superuser
        return bl_create_superuser(login, password)