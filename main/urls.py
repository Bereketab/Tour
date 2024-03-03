from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DestinationsViewSet, ServicesViewSet
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

# Define urlpatterns for regular views
urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create a router for DRF views
router = DefaultRouter()
router.register(r'api/destinations', DestinationsViewSet)
router.register(r'api/services', ServicesViewSet)

# Include DRF URLs under a specific namespace
urlpatterns += [
    path('api/', include(router.urls)),
]