Application
=================

Application is a simple django app that provides the opportunity to take tests in programming in different languages such as Python2.x, Python3.x, Java, C, C#, Perl and etc. The actual code of the app implements a sample application with tests, demo project and documentation.

It runs under officially Django https://www.djangoproject.com/:

* Django 1.11.5
* Python 3.5.2

This tutorial passes through all the steps to build the app.

Before reading this tutorial visit the official Django project website and read the tutorial on `how to write reusable apps <https://docs.djangoproject.com/en/1.11/intro/reusable-apps/>`_.


Current features
===============
* Question order randomisation
* The user authorization system
* Multiple choice question type
* Optimized admin panel
* Sqlite3 database


Directory layout
================

Application's directory structure looks as follows::

    test_service/
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    ├── db.sqlite3
    ├── docs/
    ├── application/
    │	├── __init__.py
    │	├── settings.py
    │	├── [local_settings.py]
    │   ├── urls.py
    │	└── wsgi.py
    ├── home/
    │    ├── forms/
    │    ├── migrations/
    │    ├── templates/
    │    │   └── home/
    │    ├── static/
    │    │   └── home/
    │	 ├── __init__.py
    │	 ├── admin.py
    │	 ├── apps.py
    │	 ├── models.py
    │	 ├── tests.py
    │    ├── urls.py
    │	 └── views.py
    └── quiz/
         ├── forms/
         ├── migrations/
         ├── templates/
         │   └── quiz/
         ├── static/
         │   └── quiz/
    	 ├── __init__.py
    	 ├── admin.py
    	 ├── apps.py
    	 ├── models.py
    	 ├── tests.py
         ├── urls.py
    	 └── views.py


How to launch the application on your local machie?
================
1. Install the latest virtualenv
* pip install virtualenv
* virtualenv .env

2. Activate virtualenv script
* source .env/bin/activate

3. Clone git repository
* https://github.com/stratopedarx/test_service.git
* cd test_service

4. Install all dependencies by running the following command:
* pip install -r requirements.txt

5. There are several commands which you will use to interact with migrations and Django’s handling of database schema:
* python manage.py makemigrations
* python manage.py migrate

6. Launch the application:
* python manage.py runserver

7. Check the following url: http://127.0.0.1:8000/

8. Run all tests:
* ./manage.py test