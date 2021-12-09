from django.urls import path, include

from .views      import SignUpView, SignInView, SubscribeView, UserListView, UserProfileView
from .views      import PublicUserView, PrivateUserView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/', UserListView.as_view()),
    path('/public/user/<int:user_id>', PublicUserView.as_view()),
    path('/private/user', PrivateUserView.as_view()),
]
