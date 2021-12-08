import json

from django.views import View
from django.http  import JsonResponse
from django.db.models import Count
from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        limit  = int(request.GET.get('limit', 15))
        offset = int(request.GET.get('offset', 0))

        user_tag = list(UserTag.objects.annotate(total=Count('usersusertags__user_tag_id')).values('id', 'name', 'total').order_by('-total')[offset:limit])

        return JsonResponse({'result' : user_tag}, status=200)

