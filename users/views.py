import json, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models      import User
from my_settings  import SECRET_KEY, ALGORITHM
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

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email = data.get('email')
            phone_number = data.get('phone_number')

            if User.objects.filter(email=email).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email=email).password.encode('utf-8')):
                    token = jwt.encode({'id':User.objects.get(email=email).id}, SECRET_KEY, algorithm=ALGORITHM)
                    return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN':token}, status=200)
                    
            if User.objects.filter(phone_number=phone_number).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(phone_number=phone_number).password.encode('utf-8')):
                    token = jwt.encode({'id':User.objects.get(phone_number=phone_number).id}, SECRET_KEY, algorithm=ALGORITHM)
                    return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN':token}, status=200)
            
            return JsonResponse({'message':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)


        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)