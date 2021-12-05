from django.urls import path, include

from .views      import SignUpView, SignInView
from .views      import UserListView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/', UserListView.as_view())
]
