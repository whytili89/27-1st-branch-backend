from django.urls import path
from .views      import PostListView

urlpatterns = [
    path('/<int:keyword_id>', PostListView.as_view()),
]