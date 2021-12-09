from django.urls import path, include

from .views      import PostListView
from .views      import PostView

urlpatterns=[
    path('', include([
        path('', PostListView.as_view()),
        path('/<int:keyword_id>', PostListView.as_view()),
    ])),
    path('/datail/<int:posting_id>', PostView.as_view()),
]
