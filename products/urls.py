from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductAPIView

router = SimpleRouter()
router.register("", ProductAPIView, basename='product')

urlpatterns = [

]
urlpatterns += router.urls
