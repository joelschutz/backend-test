import bcrypt
from pymodm.fields import CharField, IntegerField, EmailField, MongoBaseField
from uuid import uuid4

from app.models import BaseModel

class PasswordField(MongoBaseField):
    def __set__(self, inst, value: str):
        value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt(10))
        inst._data.set_mongo_value(self.attname, value)

class UserModel(BaseModel):
    id = CharField(default=uuid4, primary_key=True, blank=False)
    name = CharField(max_length=50, blank=False)
    email = EmailField(blank=False)
    phone = IntegerField(min_value= 1000000000, blank=False)
    password = PasswordField(validators=[lambda v: isinstance(v, str)], blank=False)
    score_count = IntegerField(default=1, blank=False)
    user_type = CharField(default='user', blank=False)

    def check_password_match(self, given_password: str):
        given_password = given_password.encode('utf-8')

        return bcrypt.checkpw(given_password, self.password)