from django.urls import path

from .views      import PostListView
from .views      import PostView
from .views       import CommentView

urlpatterns=[
    path('/<int:keyword_id>', PostListView.as_view()),
    path('/detail/<int:posting_id>', PostView.as_view()),
    path('/<int:posting_id>/comment', CommentView.as_view()),
    path('/<int:comment_id>/delete', CommentView.as_view()),
]
