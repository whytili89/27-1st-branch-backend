from django.urls import path

from .views      import UserTagListView

urlpatterns = [
    path('/userTagList', UserTagListView.as_view()),
]
