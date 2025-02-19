INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee', 
    'rest_framework', 
]

DATABASES = {
    'default':{    
                    'AUTOCOMMIT': True,
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME':"postgres",
                    'USER': "postgres",
                    'PASSWORD':"postgres",
                    'HOST':"localhost",
                    'PORT':"5433",
                 },    
 
}
