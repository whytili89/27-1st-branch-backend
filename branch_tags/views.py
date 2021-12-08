import json

from django.views import View
from django.http  import JsonResponse
from django.db.models import Count
from .models import UserTag

class UserTagListView(View) :
    def get(self, request) :
        limit  = int(request.GET.get('limit', 15))
        offset = int(request.GET.get('offset', 0))

        user_tag     = UserTag.objects.annotate(total=Count('usersusertags__user_tag_id')).order_by('-total')[offset:limit]

        userTag_list = [{'id' : userTag.id, 'tag_name' : userTag.name} for userTag in user_tag]

        return JsonResponse({'result' : userTag_list}, status=200)

