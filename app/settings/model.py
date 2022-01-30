import os
import toml
from pathlib import Path
from pydantic import BaseSettings, Field

from app.utils.converters import kebab_to_title


class Settings(BaseSettings):
    # ----------------ENVIRONMENT---------------
    ENVIRONMENT: str = Field('test', env='ENVIRONMENT')
    DEBUG: bool = True
    LOG_LEVEL: str = 'info'

    # ------------------PROJECT-----------------
    VERSION: str = None
    TITLE: str = None
    DESCRIPTION: str = None
    PORT: int = 8080
    HOST: str = '0.0.0.0'

    # --------------------APP-=-----------------
    PROJECT_KEY: str = Field(..., env='PROJECT_KEY')
    TOKEN_LIFESPAM_IN_HOURS: int = Field(24, env='TOKEN_LIFESPAM_IN_HOURS')

    # ------------------DATABASE----------------
    MONGODB_URI: str = Field(...)

    class Config:
        env_file = Path(__file__).parent.parent.parent.joinpath('.env')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        pyproject = toml.load(Path(__file__).parent.parent.parent.joinpath('pyproject.toml'))
        pyproject = pyproject.get('tool', {}).get('poetry', {})

        if not self.VERSION:
            self.VERSION = pyproject.get('version')

        if not self.DESCRIPTION:
            self.DESCRIPTION = pyproject.get('description')

        if not self.TITLE:
            self.TITLE = kebab_to_title(pyproject.get('name'))

class TestSettings(Settings):
    class Config:
        env_prefix = 'TEST_'


class LocalSettings(Settings):
    class Config:
        env_prefix = 'LOCAL_'


class DevelopmentSettings(Settings):
    class Config:
        env_prefix = 'DEV_'


class ProductionSettings(Settings):
    class Config:
        env_prefix = 'PROD_'
