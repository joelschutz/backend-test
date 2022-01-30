from pymongo.write_concern import WriteConcern
from app.settings import settings

from pymodm import MongoModel


class BaseModel(MongoModel):

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = settings.TITLE
