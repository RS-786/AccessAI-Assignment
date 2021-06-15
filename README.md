# AccessAI-Assignment

Description:
This is a CRUD application made with Django Framework.
Users can Create, Read, Update and Delete Employee records.

Features:
-> Along with these 4 options, the application also allows users to SignUp and SignIn
-> All views other than Read require the user to be logged in
-> The Read view is paginated (max 5 employees per page)
-> For updating and deleting records, user can search the employee by name, which has been made the primary key.


How to run locally:

1. Clone this repository on your local machine
2. Install django framework using pip
3. In the project directory, open cmd and run command "python manage.py runserver"


How To Deploy (on heroku):

A complete guide can be found here : 
https://www.geeksforgeeks.org/how-to-deploy-django-application-on-heroku/
