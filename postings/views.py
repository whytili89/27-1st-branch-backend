import json

from django.views import View
from django.http  import JsonResponse

from .models      import Posting
from .models      import Comment
from core.utils   import login_decorator

class PostListView(View):
    def get(self, request, keyword_id):
        order_method = request.GET.get('sort_method', 'created_at')
        limit        = int(request.GET.get('limit', 100))
        offset       = int(request.GET.get('offset', 0))

        posts = Posting.objects.filter(keyword_id=keyword_id).select_related('user').order_by(order_method)[offset:limit]

        results = [{
            'title'      : post.title,
            'sub_title'  : post.sub_title,
            'content'    : post.content,
            'thumbnail'  : post.thumbnail,
            'user'       : post.user.nickname,
            'created_at' : post.created_at, 
            'tag'        : list(post.keyword.postingtag_set.values('name')) } for post in posts
            ]
        
        return JsonResponse({'result':results}, status=200)


class CommentView(View):
    @login_decorator
    def post(self,request,posting_id):
        try:
            data    = json.load(request.body)
            reply   = data['reply'] 
            user    = request.user
            
            Comment.objects.create( 
                reply   = reply,
                user    = user,
                posting = posting_id
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
             return JsonResponse({"message" : "INVALID_REPLY"}, status=401)
