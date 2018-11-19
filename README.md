# flask sqlalchemy sample

- flask
- pymysql
- sqlalchemy
- flask-sqlalchemy

```
FLASK_APP=app

pipenv run shell
>>> from app.database import db
>>> db.create_all()

pipenv run start
# http://localhost:5000/
```