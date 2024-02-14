from django.urls import path

from query_optimisation.views import OrganizationListAPIView

urlpatterns = [
    path("organizations/", OrganizationListAPIView.as_view(), name="organizations"),
]
