from django.urls import path

from .views      import KeywordListView

urlpatterns = [
    path('/list', KeywordListView.as_view()),
]
