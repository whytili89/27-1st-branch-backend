from django.views     import View
from django.http      import JsonResponse, HttpResponse

from .models          import PostingTag

class PostTagListView(View):
    def get(self, request, posting_id):

        posting_tag = PostingTag.objects.filter(postings__id=posting_id)

        results = [
            {
                'name': post_tag.name
            }    
            for post_tag in posting_tag
        ]
        
        return JsonResponse({'result':results}, status=200)