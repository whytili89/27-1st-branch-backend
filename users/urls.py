from django.urls import path
from .views      import SignUpView
from .views      import ListView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/list', ListView.as_view()),
]
