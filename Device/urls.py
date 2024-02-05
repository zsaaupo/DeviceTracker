from django.urls import path, include
from .views import ApiAddDevice, ApiAssignDevice, ApiDeviceAssignmentLog, ApiDeviceStatus

urlpatterns = [
    path('add_device/', ApiAddDevice.as_view()),
    path('assign_device/', ApiAssignDevice.as_view()),
    path('assign_device_log/', ApiDeviceAssignmentLog.as_view()),
    path('device_status/', ApiDeviceStatus.as_view()),
]
