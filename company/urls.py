from django.urls import path

from company.views import CompanyView, SearchCompanyView

urlpatterns = [
    path('', CompanyView.as_view()),
    path('/<str:keyword>', SearchCompanyView.as_view()),
]
