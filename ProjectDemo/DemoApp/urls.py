from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router =DefaultRouter()
router.register('course', views.CourseViewSet)

# /course/ GET
# /course/ POST


urlpatterns = [
    path('', include(router.urls)),
]
