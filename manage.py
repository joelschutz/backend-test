from enum import Enum
from IPython import start_ipython
from typer import Typer, Option, Argument

cli = Typer(
    help='CLI to manage API',
    no_args_is_help=True
    )

class ENV(Enum):
    test = 'test'
    local = 'local'
    dev = 'dev'
    prod = 'prod'

def _set_env(env: ENV):
    import os

    os.environ['ENVIRONMENT'] = env.value

@cli.command(help='Open an Ipython shell in the provided environment')
def shell(
    env: ENV = Argument('local', help='Desired environment')
    ):
    _set_env(env)

    start_ipython([])

@cli.command(help='Start the a API server')
def runserver(
    env: ENV = Option('dev', help='Desired environment')
    ):
    _set_env(env)

    from uvicorn import run
    from app.settings import settings

    run(
        app='app.main:api',
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        debug=settings.DEBUG,
        log_level=settings.LOG_LEVEL
        )

@cli.command(help='Creates an admin account')
def createsadmin(
    name: str,
    email: str,
    phone: str,
    password: str,
    env: ENV = Option('dev', help='Desired environment'),
    ):
    _set_env(env)

    from app import main
    from app.models.user import UserModel

    user = UserModel(
        name=name,
        phone=phone,
        password=password,
        email=email,
        user_type='admin'
    ).save()

    print(f'Admin created: {user}')

@cli.command(help='Performs pytest routine')
def pytest():
    _set_env(ENV.test)

    import pytest
    import sys

    sys.exit(pytest.main())

if __name__ == "__main__":
    cli()