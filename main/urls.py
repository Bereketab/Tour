from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DestinationsViewSet, ServicesViewSet

app_name = 'main'

# Define urlpatterns for regular views
urlpatterns = [
    path('', views.index, name='index'),
]

# Create a router for DRF views
router = DefaultRouter()
router.register(r'api/destinations', DestinationsViewSet)
router.register(r'api/services', ServicesViewSet)

# Include DRF URLs under a specific namespace
urlpatterns += [
    path('api/', include(router.urls)),
]