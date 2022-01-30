from pymodm.errors import DoesNotExist, ValidationError

from app.controllers import BaseController
from app.models.user import UserModel
from app.utils.logging import info


class UserController(BaseController):
    model = UserModel

    @classmethod
    def create_if_new(cls, new_data: dict) -> UserModel:
        is_unique_email = False

        try:
            UserModel.objects.get({'email': new_data.get('email')})
        except DoesNotExist:
            is_unique_email = True
        else:
            return {'errors': [f'Email {new_data.get("email")} already in use'], 'error_codes': [5]}
        
        return cls.create(new_data)


    @classmethod
    def create(cls, new_data: dict) -> UserModel:
        try:
            user = cls.model(**new_data).save()
        except ValidationError as e:
            return {'errors': [f'{k}: {v[0]}' for k,v in e.message.items()], 'error_codes': [6]}

        return user

    @classmethod
    def increment_score(cls, user_id):
        try:
            user:UserModel = UserModel.objects.get({'_id': user_id})
        except DoesNotExist:
            info(f'No user was found with the user id: {user_id}')
        else:
            user.update({'$inc': {'score_count': 1}})

            info(f'Score incremented for the user {user.id} to {user.score_count}')

