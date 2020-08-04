from pymongo import MongoClient
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = MongoClient('mongodb://localhost:27017/')
    return g.db['treehole']

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
