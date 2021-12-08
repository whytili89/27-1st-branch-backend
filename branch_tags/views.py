import json

from django.views import View
from django.http  import JsonResponse
from django.db import models
from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        limit  = int(request.GET.get('limit', 15))
        offset = int(request.GET.get('offset', 0))

        user_tags = list(UserTag.objects.annotate(total=models.Count('usersusertags__user_tag_id')).values("id", "name").order_by('-total')[offset:limit])

        return JsonResponse({'result' : user_tags}, status=200)

