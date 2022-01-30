# Competition Website

An website for a competition where the participants get points for inviting new participants

## Technologies

* [Python3](https://www.python.org/)
* [FastaAPI](https://fastapi.tiangolo.com/)
* [MongoDB](https://www.mongodb.com/pt-br)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
* [Typer](https://typer.tiangolo.com/)
* [Poetry](https://python-poetry.org/)

## Configuration

Before installattion keep in mind that some configurations must be set before deploy.

* PROJECT_KEY -> A random string for encryption
* DEV_MONGODB_URI -> URI for the MongoDB database in development environment
* LOCAL_MONGODB_URI -> URI for the MongoDB database in local environment
* PROD_MONGODB_URI -> URI for the MongoDB database in production environment

This configurations can be setted as environment variables or through a `.env`

Additional variables can also be set to customize the project, notice that some must be setted using the environment prefix(`DEV_`, `LOCAL_`, etc):

* PORT -> The port where the website will be exposed.(Needs prefix)
* HOST -> The address where the website will be exposed.(Needs prefix)
* TOKEN_LIFESPAM_IN_HOURS -> The time in hours that a `access_token` will be valid.

## Installation

This project uses poetry to manage dependencies. It must be installed on the machine and
the process is different for each OS. For instructions consult the [official documetnation](https://python-poetry.org/docs/#installation)

Once Poetry is intalled you can use this command in the root directory of this project to
setup your virtual environment:

```bash
poetry install
poetry shell
```

Alternatively you can use the provided `requirements.txt` file to create the virtual environment
using the native `venv` package:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Basic Usage

This project implements a CLI for interacting with its major features.
We will use it to run to create an admin account and run the server.

First we create the admin account, for example:

```bash
python3 manage.py createadmin <admin-username> <admin-email> \
<admin-phone-number> <admin-password>
```

With a admin account we can start the server. By default it will run in the Development environment, but it can be changed using the `--env`` flag:

```bash
python3 manage.py runserver --env=local
```

Use the browser to access the website in the exposed address, by default it is `http://0.0.0.0:8080`. Enjoy the competition.

## TODOS

- [ ] Unit testing implementation
- [ ] Integration testing implementation
- [ ] Docker implementation
- [ ] Code Cleanup and refactoring
- [ ] Update templates

## Notes

* Project implemented for the [Backend Challenge](/CHALENGE.md)

* Great thanks to [nofobar](https://github.com/nofoobar) for the templates and examples. Check out their [tutorials](https://www.fastapitutorial.com/) and [example project](https://github.com/nofoobar/JobBoard-Fastapi)
