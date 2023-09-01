from .models import Users
from django.contrib.auth.hashers import make_password
import secrets
import string
from .constants import DB_Status

class CreateNewUserUseCase:
    def __init__(self) -> None:
        self.alphabet = string.ascii_letters + string.digits

    def execute(self, email, user_name, password):
        if self.is_existed(email):
            return DB_Status.ALREADY_EXIST
        salt = ''.join(secrets.choice(self.alphabet) for i in range(10))
        hash = self.__hash_password(password, salt)
        print('hash password', hash)
        user = Users.objects.create(
            email=email,
            user_name = user_name,
            password = hash,
            salt = salt,
        )
        try:
            user.save()
            return DB_Status.SUCCESS
        except Exception as e:
            print(e)
            return DB_Status.INTERNAL_ERROR
        

    def __hash_password(self, password, salt):
        s1 =  make_password(password= password, salt=salt)
        s2 = make_password(password=password, salt=salt)
        print(s1 == s2)
        return s1

    def is_existed(self, email):
        try:
            user = Users.objects.get(email=email)
            return True
        except Exception as e:
            return False
