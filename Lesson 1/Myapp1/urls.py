from django.urls import path
from .views import *

urlpatterns = [
    path('register/', simple_form_view, name='register'),
    path('login/', login_view, name='login'),
]