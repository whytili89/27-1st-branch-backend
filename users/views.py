import json, re

from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models      import User
from my_settings  import SECRET_KEY
from .validation  import validate_email, validate_phone_number, validate_password

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
        
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)

            validate_email(email)
            validate_phone_number(phone_number)
            validate_password(password)

            User.objects.create(
                name          = name,
                nickname      = nickname,
                email         = email,
                password      = password,
                phone_number  = phone_number,
                github        = github,
                profile_photo = profile_photo,
                description   = description,
                position      = position
            )
            return JsonResponse({'message':'SUCCESS!'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class ListView(View) :
    def get(self, request) :
        users = User.objects.all()
        result = []

        if users is None :
            return JsonResponse({'MESSAGE': 'No User'}, status=200)

        for user in users :
            result.append({
                "name"         : user.name,
                "nickname"     : user.nickname,
                "email"        : user.email,
                "phone_number" : user.phone_number,
                "github"       : user.github,
                "profile_photo": user.profile_photo,
                "description"  : user.description,
                "position"     : user.position,
                "created_at"   : user.created_at
            })

        return JsonResponse({'SUCCESS': result}, status=200)
