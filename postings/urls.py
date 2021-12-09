
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
    path('/detail/<int:posting_id>', PostView.as_view()),
    path('/like', LikeView.as_view()),
    path('/<int:posting_id>/comment', CommentView.as_view()),
    path('/comment/<int:comment_id>', CommentView.as_view()),
]