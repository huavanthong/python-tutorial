# Introduction

# Table of Content
* [Project structure](#about-project-structure)
* [Configuration File]()
* [Model View]()

# Questions
## About project structure
* [What is MVT model in Django?](#mvt-model)
* [What is __init__.py file in each folder in django project?](#

## About model view
* [How many steps do you implement a model on django?](#implement-model)


## Answer Questions
### MVT Model
MVT Model is a model using Model-View-Template. There aren't controller in this model because controller stayed in Template.

### __init__.py
If you want to expose your application as package. We need to create a __init__.py file.  
This file will help django framework expose our folder to package.


### Implement model
```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
More details: [here](https://docs.djangoproject.com/en/4.0/topics/db/models/)
# Getting Started
## Install Django Framework

## Start up a project
To start up a project
```
django-admin startproject myproject
```

To get help from django framework
```
python manage.py help
```

To create a application
```
python manage.py startapp myapp
```

## Login Admin Interface
Firstly, we must migrate our models to server
```
python manage.py migrate
```

Then, we create a super user for our server
```
python manage.py createsuperuser
```

Finally, we run our server
```
python manage.py runserver
```
