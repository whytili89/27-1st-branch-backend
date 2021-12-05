from django.urls import path
from .views      import PostTagListView

urlpatterns = [
    path('/<int:posting_id>', PostTagListView.as_view()),
]