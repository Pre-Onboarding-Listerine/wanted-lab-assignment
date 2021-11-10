from django.urls import path

from company.views import CreateCompanyView, SearchCompanyView

urlpatterns = [
    path('', CreateCompanyView.as_view()),
    path('/<str:keyword>', SearchCompanyView.as_view()),
]
