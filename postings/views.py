import json

from django.views import View
from django.http  import JsonResponse

from .models      import Comment
from .models      import Posting
from core.utils   import login_decorator


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

    def get(self,request,posting_id):
        
        try:
        
            comment = Posting.objects.get(id=posting_id).comment_set.values('reply')
            user    = comment.user
        
            results= {
                "comment" : comment,
                "user"    : user.name
                }
        
            return JsonResponse({"message":"SUCCESS", "results" : results})

        except Comment.DoesNotExist:
            return JsonResponse({"message": "INVALID_COMMENT"})

