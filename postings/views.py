from django.views     import View
from django.http      import JsonResponse, HttpResponse

from .models          import Posting
from branch_tags.models import PostingTag

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

class PostView(View):
    def get(self,request,post_id):
        try:
            posting = Posting.objects.get(id=post_id)

            results = {
                "title"        : posting.title,
                "sub_title"    : posting.sub_title,
                "content"      : posting.content,
                "thumbnail"    : posting.thumbnail,
                "description"  : posting.user.description,
                "nickname"     : posting.user.nickname,
                "created_at"   : posting.created_at,
                "updated_at"   : posting.updated_at,
                "posting_tags" : list(posting.posting_tags.values("name"))
            } 

            return JsonResponse({"message": "SUCCESS", "results" : results }, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)