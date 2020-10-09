# crud_flask

simple CRUD app using flask and flask-sqlalchemy.

### Requirements

* python3
* flask
* flask-sqlalchemy

### How to install

#### Step 1

Clone the repository

```
git clone https://github.com/ricardopy/crud_flask.git
```

#### Step 2

Create and activate a virtual environment

```python
python3 -m venv venv
```

```bash
source venv/bin/activate
```

#### Step 3

install flask

```python
pip3 install flask
```

#### Step 4

Install flask-sqlalchemy

```python
pip3 install flask-sqlalchemy
```

#### Step 5

Create the database

```python
flask shell
```

```python
from app import db
```

```python
db.create_all()
```

#### Step 6

Start the server

```python
flask run
```