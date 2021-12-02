from django.urls import path

from .views      import SignUpView, SignInView
from .views      import ListView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/list', ListView.as_view()),
]
