
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
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python
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
In this project, pre-commit is being used as a code quality tool to help enforce coding standards and ensure code
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

By using pytest, the development team can ensure that the FastAPI application is functioning correctly and the code
changes don't break the existing functionality. The tests can be run locally before committing code to the repository,
or can be run automatically using a CI/CD pipeline.
