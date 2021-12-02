import json, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models      import User
from branch_tags.models import UserTag
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

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name          = name,
                nickname      = nickname,
                email         = email,
                password      = hashed_password,
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
            data         = json.loads(request.body)

            email        = data.get('email')
            phone_number = data.get('phone_number')
            
            if not email:
                user = User.objects.get(phone_number=phone_number)

            if not phone_number:
                user = User.objects.get(email=email)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm=ALGORITHM)
            return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN':token}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

class ListByTag(View) :
    def get(self, request, tag_id) :
        try :
            result= []
            userTag = UserTag.objects.get(id = tag_id)
            users = userTag.users.order_by('?')[:6]
            if not users.exists() :
                return JsonResponse({'MESSGE' : 'NO_USERS'})
            for user in users :
                result.append({
                    'profile_photo' : user.profile_photo,
                    'name' : user.name,
                    'position' : user.position,
                    'description' : user.description,
                    'tags' : list(user.user_tags.values('name'))
                })
            return JsonResponse({'result':result}, status=200)
        except UserTag.DoesNotExist :
            return JsonResponse({'MESSAGE' : 'USER_TAG_DOES_NOT_EXSIT'}, status=400)