import jwt
from fastapi import Cookie, Form
from datetime import datetime, timedelta
from pymodm.errors import DoesNotExist

from app.settings import settings
from app.models.user import UserModel

class AuthController:
    project_key: str = settings.PROJECT_KEY
    token_lifespam: int = settings.TOKEN_LIFESPAM_IN_HOURS

    @classmethod
    def auth_user_with_token(cls, access_token: str=Cookie(None)):
        if not access_token:
            return {'error_codes': [5]}

        try:
            decoded_token = jwt.decode(
                access_token,
                cls.project_key,
                algorithms=["HS512"]
            ).get("sub")
            return UserModel.objects.get({'_id': decoded_token.get('id')})

        except jwt.ExpiredSignatureError:
            return {'errors': ['Token expired'], 'error_codes': [1]}

        except jwt.PyJWTError:
            return {'errors': ['Can\'t decode token'], 'error_codes': [2]}

        except DoesNotExist:
            return {'errors': ['User not found'], 'error_codes': [3]}

    @classmethod
    def auth_user_with_credentials(cls, email: str=Form(...), password: str=Form(...)):
        try:
            user = UserModel.objects.get({'email': email})
        except DoesNotExist:
            return {'errors': ['User not found'], 'error_codes': [3]}

        if user.check_password_match(password):
            return user
        else:
            return {'errors': ['Wrong password'], 'error_codes': [4]}

    @classmethod
    def create_token(cls, user: UserModel):
        data = {
            "sub": {
                "id": user.id,
            },
            "exp": datetime.utcnow() + timedelta(hours=cls.token_lifespam),
        }
        token = jwt.encode(data, cls.project_key, algorithm="HS512")
        return token