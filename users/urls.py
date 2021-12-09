from django.urls import path, include

from .views      import SignUpView, SignInView, SubscribeView, UserListView, UserProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/', UserListView.as_view()),
    path('/<int:user_id>', UserProfileView.as_view()),
    path('/subscribe', SubscribeView.as_view()),
]
