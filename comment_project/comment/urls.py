from django.urls import path
from . import views

urlpatterns = [
	path('', views.comment_list, name='comments'),
	path('delete/<int:id>', views.comment_delete, name='delete'),
	path('edit/<int:id>', views.comment_edit, name='edit'),
]

