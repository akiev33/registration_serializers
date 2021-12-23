from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GenderAPIView

router = SimpleRouter()
router.register("", GenderAPIView, basename='gender' )

urlpatterns = []
urlpatterns += router.urls