# Address Book Application

## Project

A web-based address book which allows a user to manage individual contacts.
A contact should consist of the following details (additional details are optional):

* First Name
* Last Name
* Phone Number
* Email Address
* Street Address

## User Stories

A user should be able to sign into the application.  
A user should be able to sign out of the application.  
Once a user is authenticated, the user should be able to create a new contact.  
Once a user is authenticated, the user should be able to view a contact.  
Once a user is authenticated, the user should be able to delete a contact.  
Once a user is authenticated, the user should be able to view all contacts.  
Once a user is authenticated, the user should be able to view, search, and/or ﬁlter contacts.

## Requirements

* [Python 3.7.5](https://www.python.org/)
* [Django 2.2.5](https://www.djangoproject.com/download/)
* ```pip install -r requirements.txt```

## Installation

To create a database.

    python manage.py migrate

To create a superuser - a user account that has control over everything on the site.

    python manage.py createsuperuser

Starting the web server.

    python manage.py runserver

## Website link:

http://lsaaddressbook.pythonanywhere.com/
