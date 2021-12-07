import json

<<<<<<< HEAD
from django.views import View
from django.http  import JsonResponse

from .models      import Posting
from .models      import Comment
from core.utils   import login_decorator
=======
from .models          import Posting
from branch_tags.models import PostingTag
>>>>>>> main

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

<<<<<<< HEAD

class CommentView(View):
    @login_decorator
    def post(self,request,posting_id):
        try:
            data    = json.loads(request.body)

            posting= Posting.objects.get(id=posting_id)
            reply   = data['reply'] 
            user    = request.user
            
            Comment.objects.create( 
                reply   = reply,
                user    = user,
                posting = posting
            )

            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
             return JsonResponse({"message" : "INVALID_REPLY"}, status=401)

        except Posting.DoesNotExist:
            return JsonResponse({"message": "POSTING_INVALID"}, status=400)     
    
    def get(self,request,posting_id):
        try:
        
            comment = Posting.objects.get(id=posting_id).comment_set.values('reply')
            
            results= {
                "comment" : list(comment)

            }
            return JsonResponse({"message":"SUCCESS", "results" : results}, status=201)
        
        except Comment.DoesNotExist:
            return JsonResponse({"message": "INVALID_COMMENT"}, status=401)


=======
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
>>>>>>> main
