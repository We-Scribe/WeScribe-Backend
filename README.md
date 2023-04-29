<h1 align="center">WeScribe Backend</h1>

![Django Version](https://img.shields.io/badge/Django-3.1.6-brightgreen) ![Django Rest](https://img.shields.io/badge/Django%20rest%20framework-3.12.2-brightgreen)

### Installation

	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	cd backend
	python3 manage.py makemigrations
	python3 manage.py migrate

### Run the application

	python3 manage.py runserver

### Sample credentials

	Username: admin
	Password: admin@1234

## About the repo

This is the backend of WeScribe website.

### API Documentation:
-----------------

i. User - Registration
Create/ Register a new user.

	Endpoint 	: /register/


ii. User - Details
Update user details/ Delete user.

	Endpoint	: /users/<username>

iii. Update Password
Reset Password of logged in user.

	Endpoint	: /users/<username>/reset-password

iv. Notes
Create new notes.

	Endpoint	: /notes/

v. Notes - Details
Update notes details/ Delete notes.

	Endpoint	: /notes/details/<id>

vi. User - Notes
Displays all the notes of a particular user.

	Endpoint	: /user/<username>/notes

### Other Details

Database used - Sqlite3

## Show your support

Give a ⭐️ if you like the project!