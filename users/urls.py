from django.urls import path

from .views      import ListView
from .views      import SignUpView

urlpatterns = [
    path('/list', ListView.as_view()),
    path('/signup', SignUpView.as_view()),
]
