import json

from django.views  import View
from django.http import JsonResponse

from users.models import User

class ListView(View) :
    def get(self, request) :
        users = User.objects.all()
        result = []

        if users is None :
            return JsonResponse({'MESSAGE': 'No User'}, status=200)

        for user in users :
            result.append({
                "name"         : user.name,
                "nickname"     : user.nickname,
                "email"        : user.email,
                "phone_number" : user.phone_number,
                "github"       : user.github,
                "profile_photo": user.profile_photo,
                "description"  : user.description,
                "position"     : user.position,
                "created_at"   : user.created_at
            })

        return JsonResponse({'SUCCESS': result}, status=200)
