from django.urls import path
from company.views import CompanyDetailView

urlpatterns = [
    path('/Wantedlab', CompanyDetailView.as_view()),
]