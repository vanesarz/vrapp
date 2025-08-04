from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
]