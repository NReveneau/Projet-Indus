Balafon : standalone example project
===============================================

balafon is a CRM developped in Python and Django. See https://github.com/ljean/balafon


Install
=======

Clone this project in a project folder on your machine

It is recommended to create a virtualenv for your project

    pip install django==1.8.9

    pip install balafon

    pip install django-modeltranslation

    python manage.py migrate

    python manage.py sync_translation_fields

    python manage.py createsuperuser


Run in development mode
=======

    python manage.py runserver


License
=======

CeCCIL 2.1. see balafon licensing