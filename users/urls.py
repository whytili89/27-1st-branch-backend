from django.urls import path
<<<<<<< HEAD
from .views      import SignUpView, SignInView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view())
]
=======
from .views      import SignUpView
from .views      import MyPageView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/<int:user_id>', MyPageView.as_view())
]
>>>>>>> 376aa32 (modify: .gitignore에 csv추가)
