# Server

### Tech Stack
The server uses the following technologies:
- [FastAPI](https://fastapi.tiangolo.com/) for the async REST API framework
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) for the ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) for the schemas
- [Uvicorn](https://www.uvicorn.org/) for the ASGI application
- [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) for containerizing the application

### Get Started

In order to run the server, you will need to install [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/).
Once you have these installed, clone the `backend` branch and run the containers
- `git clone -b backend --single-branch https://github.com/Saakshaat/umass-match/`
- `cd server`
- `docker-compose -f docker-compose.test.yml up --build` We use `docker-compose.test.yml` only in staging and the `--build` flag is only required when running the services for the first time 

This should start the database service which starts a Postgres instance and the uvicorn server on port 80, which should now be accessible on localhost.

