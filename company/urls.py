from django.urls import path
from company.views import CompanyCreateView

urlpatterns = [
    path("/companies", CompanyCreateView.as_view()),
]