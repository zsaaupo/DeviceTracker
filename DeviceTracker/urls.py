from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('company/', include("Company.urls")),
    path('device/', include("Device.urls")),
    path('admin/', admin.site.urls),
]
