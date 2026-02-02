from django.urls import path
from .views import HomeView, DemoView, TemplateDemo, AboutView

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('demo/', DemoView.as_view(), name='demo'),
	path('template/', TemplateDemo.as_view(), name='template'),
	path('about/', AboutView.as_view(), name='about'),

]