# 
- (t3h-python) C:\PythonT3h>conda activate t3h-python
- (t3h-python) C:\PythonT3h>code Django
- C:\Users\All Users\MySQL\MySQL Server 8.0\my.ini
# Start PRJ
- pip install django
- django-admin startproject mysite .
- python manage.py runserver

# Connect DB(C1)
### Setting
- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'root',
        'PASSWORD': '2012',
        'HOST': '127.0.0.1',
        'PORT' : '3306'
    }
}
### cmd
- pip install mysqlclient
- python manage.py migrate
# Connect DB(C2)

### Creat file db.cnf
- [client]
database=mysite
user=root
password=2012
default-character-set=utf-8

### setting
- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': './db.cnf'
        }
    }
}

# Create superuser
### cmd
- python manage.py createsuperuser
- python manage.py runserver

# Create new webapp
1. ### cmd
- python manage.py startapp home
2. ### setting
- khai báo 'home' ở "INSTALLED_APPS"
3. ## URLs in mysite
- +include
4. ## Create urls.py in home
- from django.urls import path
- from . import views
urlpatterns = [
    path('',views.home())
]
5. ## return render in view
-
6. ## Models



