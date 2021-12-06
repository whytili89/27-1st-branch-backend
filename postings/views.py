import json

from django.views import View
from django.http  import JsonResponse

from .models      import Comment
from .models      import Posting


class CommentView(View):
    def post(self,request,post_id):
        try:
            data    = json.load(request.body)
            
            reply   = data['reply'] 
            user    = request.user
            posting = Posting.objects.get(id=post_id)

            Comment.objects.create( 
                reply   = reply,
                user    = user,
                posting = posting
            )

        except KeyError:
             return JsonResponse({"message" : "INVALID_"})
