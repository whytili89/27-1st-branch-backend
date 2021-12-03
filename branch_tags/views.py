import json

from django.views import View
from django.http  import JsonResponse

from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        user_tag = UserTag.objects.all()

        if user_tag is None :
            return JsonResponse({'MESSAGE' : 'NO_USER_TAG'})

        userTag_list = [{'tag_name' : userTag.name} for userTag in user_tag]

        return JsonResponse({'result' : userTag_list}, status=200)

