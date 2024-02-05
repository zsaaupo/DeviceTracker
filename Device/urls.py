from django.urls import path, include
from .views import ApiAddDevice, ApiAssignDevice, ApiDeviceAssignmentLog

urlpatterns = [
    path('add_device/', ApiAddDevice.as_view()),
    path('assign_device/', ApiAssignDevice.as_view()),
    path('assign_device_log/', ApiDeviceAssignmentLog.as_view())
]
