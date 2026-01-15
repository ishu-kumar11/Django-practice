from django.urls import path
from .views import upload_photo, success, photo_list, photo_detail

urlpatterns = [
    path('', upload_photo, name='upload'),
    path('success/<int:id>/', success, name='success'),
    path('photos/', photo_list, name='photo_list'),
    path('photo/<int:id>/', photo_detail, name='photo_detail'),

]
