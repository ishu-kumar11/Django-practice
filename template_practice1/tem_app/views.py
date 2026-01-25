from django.shortcuts import render
from datetime import datetime

# Create your views here.

#simple template uses
def home(request):
	data = {
		'name': 'Ishu',
		'age': 19,
		'course': 'BCA',
		"today": datetime.now()
	}
	return render(request, 'tem_app/home.html', data)

#if-else statement uses
def demo(request):
	message = {
		'name': 'Ishu',
		'is_logged_in': False
	}
	return render(request, 'tem_app/demo.html', message)

def for_loop_demo(request):
	message = {
		'subjects': ['Django', 'Mongodb', 'CS', 'Java', 'Html', 'Css']
	}
	return render(request, 'tem_app/demo.html', message)

def skills(request):
	message = {
		'name': 'Ishu',
		'course': 'BCA',
		'skill': ['HTML', 'CSS', 'JavaScript', 'Django']
	}
	return render(request, 'tem_app/ishu.html', message)

def about(request):
	return render(request, 'tem_app/about.html', {'name': 'Ishu'})

def contact(request):
	return render(request, 'tem_app/contact.html', {'name': 'Ishu'})