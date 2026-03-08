from fastapi import Request
from sqlalchemy.orm import DeclarativeBase, DeferredReflection


class Base(DeclarativeBase):
    pass


class Reflected(DeferredReflection, Base):
    __abstract__ = True


def get_db(request: Request):
    session = request.app.state.session_factory()
    try:
        yield session
    finally:
        session.close()
