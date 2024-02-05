from django.urls import path, include
from .views import ApiCreateCompany, ApiNewEmployee


urlpatterns = [
    path('add_company/', ApiCreateCompany.as_view()),
    path('add_employee/', ApiNewEmployee.as_view())
]
