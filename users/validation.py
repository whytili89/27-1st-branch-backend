import re

from django.core.exceptions import ValidationError

REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
REGEX_PHONE_NUMBER = '^01[016789]{1}-?([0-9]{3,4})-?[0-9]{4}$'
REGEX_PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

def validation_email(email):
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError({'message': 'INVALID_EMAIL'}, status=400)

def validation_phone_number(phone_number):
    if not re.match(REGEX_PHONE_NUMBER, phone_number):
        raise ValidationError({'message': 'INVALID_PHONE_NUMBER'}, status=400)

def validation_password(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError({'message':'INVALID_PASSWORD'}, status=400)