from django.urls import path, include

from .views      import SignUpView, SignInView
from .views      import UserListView
from .views      import UserProfileView, MyProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/', UserListView.as_view()),
    path('/<int:user_id>', UserProfileView.as_view()),
    path('/mypage', MyProfileView.as_view()),
]
