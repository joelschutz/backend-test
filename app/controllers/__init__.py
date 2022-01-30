from abc import ABC, abstractmethod
from typing import List, Union
from app.models import BaseModel
from pymodm.connection import connect
from app.settings import settings


class BaseController(ABC):

    model = BaseModel

    def __init__(self) -> None:
        super().__init__()
        connect(settings.MONGODB_URI, settings.TITLE)

    @abstractmethod
    def get(cls, id: int, raw: bool = False) -> Union[BaseModel, dict]:
        '''
        Returns the Document with the given ID
        If no Document is found it raises a DoesNotExist error.

        raw: returns an instance of the object instead of dict, its used internally in this class
        '''

    @abstractmethod
    def fetch(
        cls,
        filters: dict = None,
        offset: int = 0,
        size: int = 20,
        raw: bool = False
    ) -> List[Union[BaseModel, dict]]:
        '''
        Returns a list of Documents queried with the given filters.

        filters: a dict of the filters to be used in the query
        offset: the number of documents to offset in the query result, it is used for pagination
        size: the number of documents to be returned, it is used for pagination
        raw: returns an instance of the object instead of dict, its used internally in this class
        '''

    @abstractmethod
    def update(
        cls,
        id: int,
        new_data: dict,
        raw: bool = False
    ) -> Union[BaseModel, dict]:
        '''
        Updates the Document with the given ID and returns it.
        If no Document is found it raises a DoesNotExist error.

        raw: returns an instance of the object instead of dict, its used internally in this class
        '''

    @abstractmethod
    def create(cls, new_data: dict, raw: bool = False) -> Union[BaseModel, dict]:
        '''
        Creates a new Document with the given data.
        If another Document with the same ID already exists it raises an OperationError error.

        raw: returns an instance of the object instead of dict, its used internally in this class
        '''

    @abstractmethod
    def delete(cls, id: int) -> None:
        '''
        Deletes the Document with the given ID.
        If no Document is found it raises a DoesNotExist error.
        '''
