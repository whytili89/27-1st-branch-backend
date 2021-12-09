
from postings.models import Like
from django.urls import path, include

from .views      import LikeView, PostListView
from .views      import PostView
from .views      import CommentView

urlpatterns=[
    path('', include([
        path('', PostListView.as_view()),
        path('/<int:keyword_id>', PostListView.as_view()),
    ])),
    path('/datail/<int:posting_id>', PostView.as_view()),
    path('/like', LikeView.as_view()),
    path('/<int:posting_id>/comment', CommentView.as_view()),
    path('/<int:comment_id>/delete', CommentView.as_view()),
]