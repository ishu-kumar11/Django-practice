from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submit/", views.submit_form, name="submit_form"),

    path("msg/success/", views.msg_success, name="msg_success"),
    path("msg/error/", views.msg_error, name="msg_error"),
    path("msg/warning/", views.msg_warning, name="msg_warning"),
    path("msg/info/", views.msg_info, name="msg_info"),
    path("msg/add-message/", views.msg_add_message, name="msg_add_message"),
]
