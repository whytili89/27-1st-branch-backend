import json, bcrypt, jwt

from django.core.exceptions import ValidationError
from django.views           import View
from django.http            import JsonResponse
from django.db.models import Count, Q, Subquery, OuterRef

from .models      import User, Subscribe
from branch_tags.models import UserTag
from postings.models import Posting

from my_settings  import SECRET_KEY, ALGORITHM
from .validation  import validate_email, validate_phone_number, validate_password
from core.utils import login_decorator

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
        except ValidationError as e:
            return JsonResponse({'message': e.message}, status=400)

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
        except ValidationError as e:
            return JsonResponse({'message': e.message}, status=400)

class PublicUserView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            result = {
                "user_id"      : user.id,
                "name"         : user.name,
                "nickname"     : user.nickname,
                "email"        : user.email,
                "description"  : user.description,
                "position"     : user.position,
                "github"       : user.github,
                "profile_photo": user.profile_photo
            }
            return JsonResponse({"message" : "SUCCESS", "result" : result}, status=200)
        
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)


    
    def post(self, request, user_id):
        try:
            data               = json.loads(request.body)
            user               = User.objects.get(id = user_id)
            email              = data.get("email", user.email)
            phone_number       = data.get("phone_number", user.phone_number)
            
            validate_email(email)
            validate_phone_number(phone_number)
            
            user.name          = data.get("name", user.name)
            user.nickname      = data.get("nickname", user.nickname)
            user.email         = email
            user.description   = data.get("description", user.description)
            user.position      = data.get("position", user.position)
            user.github        = data.get("github", user.position)
            user.profile_photo = data.get("profile_photo", user.position)
            user.phone_number  = phone_number
            user.save()
            
            return JsonResponse({"message":"SUCCESS"}, status=201) 
        
        except ValidationError: 
            return JsonResponse({"message" : "INVALID_VALUE"}, status=400)

class UserListView(View) :
    def get(self, request) :
        limit       = int(request.GET.get('limit', 6))
        offset      = int(request.GET.get('offset', 0))
        user_tag_id = request.GET.get('user_tag_id', None)
        keyword_id  = request.GET.get('keyword_id', None)

        q = Q()
        if keyword_id:
            q &= Q(posting__keyword_id=keyword_id)

        if user_tag_id:
            q &= Q(user_tags__id=user_tag_id)

        user_list_subquery = Posting.objects.filter(user_id=OuterRef('pk')).values('user_id').annotate(total_posting=Count('id')).values('total_posting')
        users= User.objects.annotate(total_posting=Subquery(user_list_subquery)).filter(q).order_by('-total_posting')[offset:limit]

        results =[{
            'user_id'      : user.id,
            'profile_photo': user.profile_photo,
            'name'         : user.name,
            'position'     : user.position,
            'description'  : user.description,
            'posting_count': user.total_posting,
            'tags'         : list(user.user_tags.values('id', 'name'))
        } for user in users]

        return JsonResponse({'SUCCESS': results}, status=200)

class PrivateUserView(View):
    @login_decorator
    def get(self, request):
        result = {
            "user_id"      : request.user.id,
            "name"         : request.user.name,
            "nickname"     : request.user.nickname,
            "email"        : request.user.email,
            "description"  : request.user.description,
            "position"     : request.user.position,
            "github"       : request.user.github,
            "profile_photo": request.user.profile_photo
            }
        
        return JsonResponse({"message" : "SUCCESS", "result" : result}, status=200)
    
class SubscribeView(View) :
    @login_decorator
    def post(self, request) :
        try : 
            data = json.loads(request.body)

            subscribing = request.user
            subscriber = User.objects.get(id=data['subscriber_id'])

            if subscribing.id == subscriber.id :
                return JsonResponse({'MESSAGE' : 'YOU_CAN_NOT_SUBSCRIBE_YOURSELF'}, status=400)
            subscribed, created = Subscribe.objects.get_or_create(subscribing= subscribing, subscriber= subscriber)

            if not created :
                subscribed.delete()
                return JsonResponse({'SUCCESS':'UNSUBSCRIBED'}, status=201)
            return JsonResponse({'SUCCESS':'SUBSCRIBED!'}, status=201)
                
        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist :
            return JsonResponse({'MESSAGE' : 'USER_DOSE_NOT_EXIST'}, status=400)

