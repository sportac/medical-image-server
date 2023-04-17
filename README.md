
# Medical Image Server
The Medical Image Server is a web application that serves as a platform for retrieving and displaying medical images
from DICOM files. The application consists of a front-end in Javascript and a back-end writen in Python and Fast Api.

## Project Setup
### Docker
This project uses Docker to containerize the application, which allows for easier deployment and reproducibility across
different environments. The main parts of the Docker setup include the Dockerfile, which defines the image that will be
built for the application, and the docker-compose.yml file, which defines the services that will run together as containers.
In our case we only have a single service acting as web server.

To start the application we use the command:
```bash
docker compose up --build
```

### Fast API
FastAPI is a web framework for building APIs with Python 3.7+ based on standard Python
type hints. It is designed to be easy to use and to provide high performance, with features such as automatic validation
of request and response data, automatic generation of OpenAPI (formerly known as Swagger) documentation, and easy
integration with other tools such as databases, async libraries, and more. FastAPI is built on top of Starlette for the
web parts and Pydantic for the data parts, and is inspired by both Flask and Django.

To get started we use the command:
```bash
pip install fastapi
```
To run the server:
```bash
uvicorn main:app --reload
```
### Pre-commit
Pre-commit is being used as a code quality tool to help enforce coding standards and ensure code
consistency across the project. It is configured to run automatically before every commit, preventing code that does
not meet the defined standards from being committed.

Pre-commit achieves this by providing a framework for executing various pre-commit hooks or scripts that can perform
checks on the code. These hooks can include tools for formatting code, linting, static analysis, and more. Pre-commit
configuration can be found in ``.pre-commit-config`` and ``setup.cfg`` files.

It can be run locally using the command:
```bash
pre-commit run --all-files
```
### Pytest
Pytest is being used in this project as a testing framework to test the functionality of the FastAPI application.
Pytest allows the developer to write test functions in Python and assert expected results.

By using pytest, we can ensure that the FastAPI application is functioning correctly and the code
changes don't break the existing functionality. The tests can be run locally before committing code to the repository,
or can be run automatically using a CI/CD pipeline.

## Project Structure
### Models
The models.py file is used to define the data models that will be used to represent data
in our application's SQLite database. It defines the fields and data types for each table in the database, and specifies
the relationships between those tables.

### Schemas
The schemas.py defines the Pydantic schemas that will be used to validate
and serialize data in our application's API. It defines the fields and data types for each request and response object,
and specifies the relationships between those objects.

### Crud
The crud.py file defines the CRUD (Create, Read, Update, Delete) operations that
our application's API will perform on our User model. It provides a set of functions that interact with the database
through SQLAlchemy's Session object to perform these operations.

### Database
In this project, we are using SQLAlchemy as an Object-Relational Mapping (ORM) tool to connect our FastAPI application
to a SQLite database. SQLAlchemy is a Python library that provides a high-level interface for interacting with
relational databases, and allows developers to work with databases in a more Pythonic way, using Python objects and
syntax instead of writing raw SQL queries.

### Alembic
We use Alembic in this project as a database migration tool. Alembic helps us to keep our database schema in sync with
the changes we make to our models in a version-controlled and systematic way.

When we make changes to our database schema, such as adding or modifying tables or columns, we create a new migration
script using Alembic. This migration script contains the necessary SQL commands to apply or revert the changes to the
database. We can then run the migration script to apply the changes to our database, or revert the changes if needed.

To init alembic in the project:
```bash
alembic init alembic
```
This creates an alembic directory in the project with some configuration files and a versions directory where the
migration files are stored.

Update the alembic.ini file with:
```ini
# alembic.ini
sqlalchemy.url = DATABASE_URL
```
Generate migration file:
```bash
alembic revision --autogenerate -m "Initial migration"
```
Run the migrations to the database:
```bash
alembic upgrade head
```
## Views
In the main.py file, the views are the functions that handle the HTTP requests and responses for the API endpoints.
The purpose of these views is to define the behavior of the API when it receives requests from clients.

### Create User
This view creates a new user in the database when it receives a POST request at the /users endpoint. It reads the user
data from the request body, validates it using the Pydantic schema, creates a new user object using the SQLAlchemy model,
and saves it to the database using the SQLAlchemy session.

```bash
POST /users HTTP/1.1
Content-Type: application/json

{
    "username": "sergiporta",
    "password": "mypassword",
    "email": "sergiporta@gmail.com"
}
```
### Read User
This view retrieves a user from the database when it receives a GET request at the /users/{user_id} endpoint. It reads
the user ID from the request parameters, queries the database using the SQLAlchemy session to retrieve the user with
that ID, and returns the user data as a response.

### Read Users
This view retrieves all users from the database when it receives a GET request at the /users endpoint. It queries the
database using the SQLAlchemy session to retrieve all users and returns a list of user data as a response.
