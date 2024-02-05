from django.urls import path, include
from .views import ApiAddDevice, ApiAssignDevice

urlpatterns = [
    path('add_device/', ApiAddDevice.as_view()),
    path('assign_device/', ApiAssignDevice.as_view()),
]
