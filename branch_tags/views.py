import json

from django.views import View
from django.http  import JsonResponse

from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        user_tag = UserTag.objects.all()
        userTag_list = [{'id' : userTag.id, 'tag_name' : userTag.name} for userTag in user_tag]

        return JsonResponse({'result' : userTag_list}, status=200)

