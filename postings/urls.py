from django.urls import path

from .views      import PostListView
from .views      import PostView
from .views       import CommentView

urlpatterns=[
    path('/<int:keyword_id>', PostListView.as_view()),
    path('/<int:post_id>', PostView.as_view()),
    path('/<int:posting_id>/comment', CommentView.as_view()),
]