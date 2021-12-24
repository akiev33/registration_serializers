from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BasketAPIView, BasketDeleteAPIView


router = SimpleRouter()
router.register("", BasketAPIView, basename='basket')

urlpatterns = [
    path('basket/<int:id>/', BasketDeleteAPIView.as_view()),
]
urlpatterns += router.urls