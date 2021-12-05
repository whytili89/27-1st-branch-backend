from django.views import View
from django.http  import JsonResponse

from .models import Keyword

class KeywordListView(View) :
        def get(self, request) :
            keywords = Keyword.objects.all()

            keyword_list = [{
                'keyword_id' : keyword.id,
                'name' : keyword.name} for keyword in keywords]

            return JsonResponse({'result' : keyword_list}, status=200)