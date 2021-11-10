from django.urls import path

from company.views import CreateCompanyView

urlpatterns = [
    path('', CreateCompanyView.as_view()),
    # path('/<str:keyword>', ),
]
