from logging import getLogger

from app.settings import settings
from app.utils.converters import title_to_kebab

logger = getLogger()

error = logger.error
warn = logger.warn
info = logger.info
debug = logger.debug
