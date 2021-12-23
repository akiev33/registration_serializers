from django.urls import path
from authentications.views import RegisterApiView, ActivationView, LoginApiView, LogoutApiView, ChangePasswordView


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activate_account'),
    path('logout/', LogoutApiView.as_view()),
    path('change/', ChangePasswordView.as_view())
]