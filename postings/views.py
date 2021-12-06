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
                user    = user.id,
                posting = posting_id
            )

        except KeyError:
             return JsonResponse({"message" : "INVALID_REPLY"})