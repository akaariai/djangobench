DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'akaariai',
        'USER': 'akaariai',
    },
}

SECRET_KEY = "NOT REALLY SECRET"