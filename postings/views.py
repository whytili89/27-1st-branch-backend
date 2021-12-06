import json

from django.views import View
from django.http  import JsonResponse

from .models            import Posting
from branch_tags.models import PostingTag


class PostView(View):
    def get(self,request,post_id):
        try:
            posting = Posting.objects.get(id=post_id)
            posting_tags = Posting.objects.get(id=post_id).posting_tags.values("name")
            
            
            results = {
                "title"       : posting.title,
                "created_at"  : posting.created_at,
                "content"     : posting.content,
                "description" : posting.user.description,
                "nickname"    : posting.user.nickname,
                "post_tags"   : posting_tags
            } 

            return JsonResponse({"message": "SUCCESS", "results" : results })

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)