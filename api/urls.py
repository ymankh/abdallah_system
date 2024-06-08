from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialtyViewSet, DoctorViewSet, ChildViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'specialties', SpecialtyViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'children', ChildViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
