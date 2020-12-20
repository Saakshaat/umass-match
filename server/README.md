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

### Working

The server runs when by starting uvicorn with `uvicorn main:app` which uses the `main.py` as the entrypoint to the server. This module also has the FastAPI app which includes the top-level router containing all routes, and our auth middleware dependencies.

Routes are defined in individual `api` modules and use different routers, all of which get added on top of the top-level router (`main_router`). All routes use a database session injection which is created when the server starts and is used as DI ([dependency-injection](https://en.wikipedia.org/wiki/Dependency_injection)). This session is used for all database operations.

We have a separate `crud` package which is used to handle different read and write operations and also contains a `custom` module for facilitating the matching.
The `create` module in this package has a very interesting function for automatically detecting, assessing and resolving relationships for a given object's data. This uses [SQLAlchemy's Inspector](https://docs.sqlalchemy.org/13/core/inspection.html) to identify all relationships for a model and compute the given data accordingly.

`models` and `schemas` are separated in their separate packages and their usage is more or less on-call. Tables corresponding to all models are created when the database sessions injection is created during the server's startup.

### Matching
Matches between 2 users are modelled by a `Match` model which stored ForeignKey references to the current user and the other (matched user). When the client requests a match for a given user, the server first checks if the user has been matched in the past 3 days and if so, rejects the request. The matching algorithm works in 4 parts:

1. For the given user, gets a list of all matchable users. A matchable user is someone who's not been matched with this user before (User's list of previous_matches: Match objects) and who's either not been matched ever before or in the past 3 days.

2. Using this list of matchable users and the current user's data, create a Filter object. Filter is a class implementing the FluentAPI pattern. It has methods to filter its own list of matchable users by comparing them to the current user by specific params. Each method returns the object itself (hence Fluent design).

3. A client-request for creating a match also sends, in the body, a list of booleans (profile fields) representing whether the user wants to match basis this field or not. If a boolean is true, its filter method is called on the Filter object created in (2). If any filter method results in an empty list, we disregard its result.

4. From the final filtered list, we return a random user.

After recieving the matched user, we create 2 `Match` objects for both users and update their `last_matched_time` (hence starting a cooldown for their next match) and commit all these changes to the database.
