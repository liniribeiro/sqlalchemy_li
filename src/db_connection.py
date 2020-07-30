from contextlib import contextmanager

from singleton_decorator import singleton
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from .settings import TEST
Base = declarative_base()


@singleton
class DBConnector:
    def __init__(self):
        print("Session criada")
        print(f"Teste Decouple {TEST}")
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    @contextmanager
    def conn_session(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
