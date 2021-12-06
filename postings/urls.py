from django.urls  import path

from .views       import CommentView

urlpatterns=[
    path('/<int:posting_id>/comment', CommentView.as_view())
]