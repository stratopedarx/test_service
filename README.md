Application
=================

Application is a simple django app that provides the opportunity to take tests in programming in different languages such as Python2.x, Python3.x, Java, C, C#, Perl and etc. The actual code of the app implements a sample application with tests, demo project and documentation.

It runs under officially Django https://www.djangoproject.com/:

* Django 3.0.7
* Python 3.8.3
* Linux

This tutorial passes through all the steps to build the app.


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
* git clone https://github.com/stratopedarx/test_service.git
* cd test_service/

4. Install all dependencies by running the following command:
* pip install -r requirements.txt

5. If you are going to use a new database sqlite3 run the following commands, if not then skip this step:
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser

6. Launch the application:
* python manage.py runserver

7. Check the following url: http://127.0.0.1:8000/

8. Run all tests:
* ./manage.py test