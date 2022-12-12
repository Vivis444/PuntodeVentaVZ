import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

"""POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '7410',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}"""
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 's@dfsf511',
        'HOST': 'db_postgres',
        'PORT': '5432',
    }
}