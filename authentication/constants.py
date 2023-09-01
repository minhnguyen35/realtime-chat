from enum import Enum

class DB_Status(Enum):
    ALREADY_EXIST = 1
    WRONG_PASSWORD = 2
    SUCCESS = 3
    INTERNAL_ERROR = 4
    NOT_FOUND = 5