from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PersonalAPIView

router = SimpleRouter()
router.register("", PersonalAPIView, basename='personal')

urlpatterns = [

]
urlpatterns += router.urls