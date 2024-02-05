from django.urls import path, include
from .views import ApiAddDevice

urlpatterns = [
    path('add_device/', ApiAddDevice.as_view()),
]
