from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

#making class based view

#This is simple class based view
class HomeView(View):
	def get(self, request):
		return HttpResponse("Hello This is class based views")


#this is for get and post request , by default get
class DemoView(View):
	def get(self, request):
		return HttpResponse("This is get method")

	def post(self, request):
		return HttpResponse("This is post method")


#this is template view using generic views

class TemplateDemo(TemplateView):
    template_name = "class_views_app/home.html"

    #Passing data in html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["name"] = "Ishu"
        context["msg"] = "You are learning CBV Level 2 🔥"
        context["skills"] = ["HTML", "CSS", "Python", "Django"]

        return context



#render html page in class based view using render method
class AboutView(View):
    def get(self, request):
        return render(request, "class_views_app/about.html")
