from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('demo/', views.demo, name='demo'),
	path('noname/', views.for_loop_demo, name='ishu'),
	path('skills/', views.skills, name='skills'),
	path('about/', views.about,name='about'),
	path('contact/', views.contact,name='contact'),
]