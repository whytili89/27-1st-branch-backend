from django.urls import path
from users.views import ListView

urlpatterns = [
    path('/list', ListView.as_view()),
]
