from django.views     import View
from django.http      import JsonResponse, HttpResponse

from .models          import Posting

class PostListView(View):
    def get(self, request, keyword_id):
        order_method = request.GET.get('sort_method', 'created_at')
        limit        = int(request.GET.get('limit', 10))
        offset       = int(request.GET.get('offset', 0))

        posts = Posting.objects.filter(keyword_id=keyword_id).order_by(order_method)[offset:limit]

        results = [{
            'title'      : post.title,
            'sub_title'  : post.sub_title,
            'content'    : post.content,
            'thumbnail'  : post.thumbnail,
            'user'       : post.user.nickname,
            'created_at' : post.created_at } for post in posts
            ]
        
        return JsonResponse({'result':results}, status=200)