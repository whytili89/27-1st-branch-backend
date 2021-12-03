from django.urls import path

from .views      import SignUpView, SignInView, UserProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/<int:user_id>', UserProfileView.as_view())
]