from django.urls import path, include
from .views import ApiCreateCompany


urlpatterns = [
    path('add_company/', ApiCreateCompany.as_view()),
]
