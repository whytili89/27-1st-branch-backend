import json

from django.views import View
from django.http  import JsonResponse

from .models            import Posting
from branch_tags.models import PostingTag


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

            return JsonResponse({"message": "SUCCESS", "results" : results })

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)