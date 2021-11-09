from django.urls import path
from company.views import CompanyDetailView

urlpatterns = [
    path('/<str:keyword>', CompanyDetailView.as_view()),
]