import json
from django.core.exceptions import MultipleObjectsReturned

from django.views import View
from django.http  import JsonResponse

from .models import Posting

class PostView(View):
    def get(self,request,post_id):
        try:
            posting = Posting.objects.get(id=post_id)
            results = {
                "title"       : posting.title,
                "created_at"  : posting.created_at,
                "content"     : posting.content,
                "description" : posting.user.description,
                "user_name"   : posting.user.name
            }
            return JsonResponse({"message": "SUCCESS", "results" : results })

        except Posting.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)

        except Posting.MultipleObjectsReturned:
            return JsonResponse({"message" : "INVALID_POSTING"}, status=401)
