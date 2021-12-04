from django.urls import path

from .views      import PostView


urlpatterns=[
    path('/<int:post_id>', PostView.as_view())
]