import json

from django.views import View
from django.http  import JsonResponse
from django.db.models import Q

from .models      import Posting
from .models      import Comment
from core.utils   import login_decorator

class PostListView(View):
    def get(self, request, **kwargs):
        try :  
            order_method = request.GET.get('sort_method', 'created_at')
            limit        = int(request.GET.get('limit', 100))
            offset       = int(request.GET.get('offset', 0))

            q= Q()

            if kwargs :
                q  &=Q(keyword_id=kwargs['keyword_id'])

            posts = Posting.objects.filter(q).select_related('user').order_by(order_method)[offset:limit]

            results = [{
                'id'        : post.id,
                'title'     : post.title,
                'sub_title' : post.sub_title,
                'content'   : post.content,
                'thumbnail' : post.thumbnail,
                'user'      : post.user.nickname,
                'created_at': post.created_at,
                'tag'       : list(post.keyword.postingtag_set.values('name')) } for post in posts
                ]

            return JsonResponse({'result':results}, status=200)
        except KeyError :
            return JsonResponse({'MESSGE':'KEY_ERROR'}, status=400)

class PostView(View):
    def get(self,request,posting_id):
        try:
            posting      = Posting.objects.get(id=posting_id)
            prev_posting = Posting.objects.filter(id__lt=posting_id, user_id=posting.user_id).values('id', 'title').order_by('-id')[:1]
            next_posting = Posting.objects.filter(id__gt=posting_id, user_id=posting.user_id).values('id', 'title')[:1]

            results = {
                "title"        : posting.title,
                "sub_title"    : posting.sub_title,
                "content"      : posting.content,
                "thumbnail"    : posting.thumbnail,
                "description"  : posting.user.description,
                "nickname"     : posting.user.nickname,
                "created_at"   : posting.created_at,
                "updated_at"   : posting.updated_at,
                "posting_tags" : list(posting.posting_tags.values("name")),
                "prev_posting" : prev_posting[0] if prev_posting  else None,
                "next_posting" : next_posting[0] if next_posting  else None,
            } 

            return JsonResponse({"message": "SUCCESS", "results" : results }, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)