import json, re

from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models      import User
from my_settings  import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
 
            name          = data['name']
            nickname      = data['nickname']
            email         = data['email']
            password      = data['password']
            phone_number  = data['phone_number']
            github        = data.get('github', None)
            profile_photo = data.get('profile_photo', None)
            description   = data.get('description', None)
            position      = data.get('position', None)
            subscribe     = data.get('subscribe', None)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)

            REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PHONE_NUMBER = '^01[016789]{1}-?([0-9]{3,4})-?[0-9]{4}$'
            REGEX_PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

            if not re.match(REGEX_PHONE_NUMBER, phone_number):
                return JsonResponse({'message': 'INVALID_PHONE_NUMBER'}, status=400)

            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=400)

            User.objects.create(
                name          = name,
                nickname      = nickname,
                email         = email,
                password      = password,
                phone_number  = phone_number,
                github        = github,
                profile_photo = profile_photo,
                description   = description,
                position      = position,
                subscribe     = subscribe
            )
            return JsonResponse({'message':'SUCCESS!'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
