from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


#This is home page view
def home_view(request):
	return render(request, 'myformapp/home.html')

#handle the contact form
def contact_view(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			form.send_email()
			return redirect('contact-success', name=name)
		
	form = ContactForm()
	context = {'form': form}
	return render(request, 'myformapp/contact.html', context)

def contact_success_view(request, name):
	return render(request,'myformapp/contact_success.html', {'name': name})
