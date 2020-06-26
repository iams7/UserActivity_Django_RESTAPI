# UserActivity_Django_RESTAPI
RESTAPI using Django Framework for User Activity (Backend code)

## Goal

The goal of this project is to create a API to serve User and UserActivityPeriod data models and with a custom management command to populate the database with some dummy data in the json format.

## Features

With this API;

    You can create, view, update, and delete the users

## Technology stack

Tools used during the development of this API are;

    Django - a python web framework
    Django REST Framework - a flexible toolkit to build web APIs
    Postgresql - this is a database server
    
## Build way

   1. Installed packages - django and djangorestframework
   2. Created a model (Product) object and did CRUD(Create / Read/Update/Delete) operations using django admin page
   3. Created REST API (GET, POST, PUT  and DELETE)
   4. Tested the services(API) using Postman ( tool testing APIs)
   5. Finally created some exception/error handling 


## Requirements

    Use Python 3.x.x+
    Use Django 2.x.x+

## Running the application

To run this application, clone the repository on your local machine and execute the following command.

    $ cd music_service
    $ virtualenv <virtenv>
    $ source virtenv/bin/activate OR workon <previously created virtenv>
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

Use POSTMAN API Development Environment tool and run the URL: 127.0.0.1:8000/api/product and
Try GET using 127.0.0.1:8000/api/product
POST using 127.0.0.1:8000/api/product/<ID> with new data
PUT using 127.0.0.1:8000/api/product/<ID> and 
DELETE using 127.0.0.1:8000/api/product/<ID> 

actions and send parameters to access, manipulate and retrive User Activity Data.

    If needed, you can manipulate data on the admin console.
