from django.urls import path
from authentications.views import RegisterApiView


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
]