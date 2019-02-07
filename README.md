# CRUD_Django_Example

This is a simple example explaining CRUD operations in Django

Example contains the implemention of CRUD operations using Function Based Views and Class Based Views in Djnago.

CRUD_FBVs(implementing Function Based Views) uses the built-in user Model by Django. You can also append

LOGIN_URL = '/admin/login/'

to settings.py, create super user by 'python manage.py createsuperuser' and use superuser to access this functionality or feel free to extend the repo.

IF you want to test the CRUD_CBVs(implementing Class Based Views) you can add user as Foreing key to movie model and use it same as CRUD_FBVs

#### Things to do :
1. `git clone https://github.com/hendisantika/CRUD_Django_Example.git`
2. `cd CRUD_Django_Example`
3. `python manage.py runserver`

#### Screen shot

Login Django

![Login Django Admin](img/admin.png "Login Django Admin")

Username / Password : hendisantika/hendisantika

Django Dashboard

![Django Dashboard](img/dashboard.png "Django Dashboard")

Add new Movie

![Add new Movie](img/add.png "Add New Movie")

Save new Movie

![Save new movie](img/save.png "Save new movie")

Details Data

![Details Data](img/details.png "Details Data")

Select Data

![Select Data](img/select.png "Select Data")