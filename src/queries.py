from src.migrations.upgrade import upgrade
from src.db_connection import DBConnector
from src.models.user import User


def save_user():
    with DBConnector().conn_session() as session:
        user = User(name='John Snow', password='johnspassword')
        session.add(user)


def get_user():
    with DBConnector().conn_session() as session:
        db_user = session.query(User).filter_by(name='John Snow').first()
        print(db_user)



