import json

from django.views     import View
from django.http      import JsonResponse
from json.decoder     import JSONDecodeError
from django.db.models import Q

from .models          import Posting, Like
from .models          import Comment
from core.utils       import login_decorator

class PostListView(View):
    def get(self, request, **kwargs):
        try :  
            order_method = request.GET.get('sort_method', 'created_at')
            limit        = int(request.GET.get('limit', 100))
            offset       = int(request.GET.get('offset', 0))

            q= Q()

            if kwargs :
                q  &=Q(keyword_id=kwargs['keyword_id'])

            postings = Posting.objects.filter(q).select_related('user').order_by(order_method)[offset:limit]

            results = [{
                'posting_id': posting.id,
                'title'     : posting.title,
                'sub_title' : posting.sub_title,
                'content'   : posting.content,
                'thumbnail' : posting.thumbnail,
                'user'      : posting.user.nickname,
                'created_at': posting.created_at,
                'tag'       : list(posting.keyword.postingtag_set.values('name')) } for posting in postings
                ]

            return JsonResponse({'result':results}, status=200)
        except KeyError :
            return JsonResponse({'MESSGE':'KEY_ERROR'}, status=400)

class PostView(View):
    def get(self, request, posting_id):
        try:
            posting      = Posting.objects.get(id=posting_id)
            prev_posting = Posting.objects.filter(id__lt=posting_id, user_id=posting.user_id).values('id', 'title').order_by('-id')[:1]
            next_posting = Posting.objects.filter(id__gt=posting_id, user_id=posting.user_id).values('id', 'title')[:1]

            results = {
                "posting_id"  : posting.id,
                "title"       : posting.title,
                "sub_title"   : posting.sub_title,
                "content"     : posting.content,
                "thumbnail"   : posting.thumbnail,
                "description" : posting.user.description,
                "nickname"    : posting.user.nickname,
                "created_at"  : posting.created_at,
                "updated_at"  : posting.updated_at,
                "posting_tags": list(posting.posting_tags.values("name")),
                "prev_posting": prev_posting[0] if prev_posting  else None,
                "next_posting": next_posting[0] if next_posting  else None,
            } 

            return JsonResponse({"message": "SUCCESS", "results" : results }, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)

class LikeView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            like, created = Like.objects.get_or_create(user_id = user.id, posting_id = data['posting_id'])

            if not created:
               
                like.delete()
                return JsonResponse({'message':'CANCELED_LIKE'}, status=201)
              
            return JsonResponse({'message':'SUCCESS_LIKE'}, status=200)

        except JSONDecodeError:
          return JsonResponse({'message':'JSON_DECODE_EEROR'}, status=400)

    @login_decorator
    def get(self, request):
        user    = request.user
        postings = Posting.objects.filter(like__user_id = user.id)

        try:
            postings_user_liked = [{
                'posting_id': posting.id,
                'like_count': Like.objects.filter(posting_id = posting.id).count()
            } for posting in postings]

            return JsonResponse({
                'message':'SUCCESS', 'POSTING_USER_LIKED' : postings_user_liked}, status=201
            )
        
        except AttributeError:
            return JsonResponse({'message':'AttributeError'}, status=400)
        
