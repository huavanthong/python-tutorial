#Introduction

This project introduce to you opearting with Django project.

# Table of contents

## Prepare environment
To install Django for your PC.
```

```
## Getting Started
To clone this project
```
https://github.com/nhtung96/carzone-web?fbclid=IwAR2GiUtxEk9kBNniasxEqU2owWDdSnVBf6b2MRMfn2Z5jpV70oVtseICY_4
```

Prepare the neccessary library for this project
```
pip install django-ckeditor
pip install django-multiselectfield
pip install psycopg2
python -m pip install Pillow
```

To migrate your database to PostgreSQL
```
python manage.py migrate
```

To create a superuser account for web admin.
```
python manage.py createsuperuser
```

To run this project on server
```
python manage.py runserver
```

### Open brower
To run web-admin.
```
http://127.0.0.1:8000/admin
```
**Note:**
* Account:
> admin  
> hvthong123

To see all products in this projects
```
http://127.0.0.1:8000/cars/
```
