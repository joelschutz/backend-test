import os
from app.settings.model import (
    LocalSettings,
    DevelopmentSettings,
    ProductionSettings,
    TestSettings
)

class SettingsFactory:
    @staticmethod
    def get_settings(env: str = None):
        if env is None:
            env = os.environ.get("ENVIRONMENT")

        if env == 'local':
            return LocalSettings()
        elif env == 'dev':
            return DevelopmentSettings()
        elif env == 'prod':
            return ProductionSettings()
        else:
            return TestSettings()


settings = SettingsFactory.get_settings()
