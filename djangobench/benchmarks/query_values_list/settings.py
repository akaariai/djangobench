from djangobench.base_settings import *

INSTALLED_APPS = ['query_values_list']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'akaariai',
        'USER': 'akaariai',
    },
}
