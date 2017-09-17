Application
=================

Application is a simple django app that provides the opportunity to take tests in programming in different languages such as Python2.x, Python3.x, Java, C, C#, Perl and etc. The actual code of the app implements a sample application with tests, demo project and documentation.

It runs under officially Django https://www.djangoproject.com/:

* Django 1.11.5
* Python 3.5.2

This tutorial passes through all the steps to build the app.

Before reading this tutorial visit the official Django project website and read the tutorial on `how to write reusable apps <https://docs.djangoproject.com/en/1.11/intro/reusable-apps/>`_.

Directory layout
================

Application's directory structure looks as follows::

    application/
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    ├── docs/
    ├── application/
    │	├── settings.py
    │   ├── urls.py
    │	└── wsgi.py
    └── quiz/
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── migrations/
	│   └── __init__.py
        ├── templates/
        │   └── quiz/
        │        ├──
        │        └──
        └── static/
            └── quiz/
                 ├──
                 └──


How to launch the application on your local machie?
================
1. Install all dependencies by running the following command:
* pip install -r requirements.txt


