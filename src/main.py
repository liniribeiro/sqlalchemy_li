from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.migrations import upgrade
from src.queries import save_user, get_user
from src.settings import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)
upgrade()


@app.route('/')
def hello_world():
    save_user()
    get_user()

    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
