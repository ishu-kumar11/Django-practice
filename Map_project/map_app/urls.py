from django.urls import path
from .views import location_form, success_page

urlpatterns = [
    path("", location_form, name="location_form"),
    path("success/", success_page, name="success"),
]
