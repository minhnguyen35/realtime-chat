from .models import Users
from django.contrib.auth.hashers import make_password
from .constants import DB_Status

class VerifyLoginUseCase:

    def execute(self, email, input_password):
        try:
            user = Users.objects.get(email=email)
            print(user.salt)
            hash_input = make_password(input_password, user.salt)
            print('input pass: ',hash_input)
            print('db pass: ', user.password)
            if hash_input == user.password:
                return DB_Status.SUCCESS
            else:
                return DB_Status.WRONG_PASSWORD
        except:
            return DB_Status.NOT_FOUND
