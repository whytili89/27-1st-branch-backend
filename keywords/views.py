from django.views import View
from django.http  import JsonResponse

from .models import Keyword

class KeywordListView(View) :
        def get(self, request) :

            return JsonResponse({'result' : list(Keyword.objects.values('id', 'name'))}, status=200)