from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ApplicationViewSet
from courses.views import CourseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]