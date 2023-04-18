SECRET_KEY = "@2cbz02t%dmi1t5w_hycfym+1v5pqq!yj9(pj*i!1v_zbbxg$)"
DEBUG = True
STATIC_ROOT = '/app/statifiles'
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
