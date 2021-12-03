import json

from django.views import View
from django.http  import JsonResponse

from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        userTags = UserTag.objects.all()

        if userTags is None : 
            return JsonResponse({'MESSAGE' : 'NO_USER_TAG'})

        userTag_list = [{'tag_name' : userTag.name} for userTag in userTags]

        return JsonResponse({'result' : userTag_list}, status=200)

