from django.shortcuts import render, redirect
from .forms import RegsiterForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
	if request.method == 'POST':
		form = RegsiterForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			return redirect('login')

	else:
		form = RegsiterForm()

	return render(request, 'accounts/register.html' , {'form': form})



def login_view(request):
	error = ""

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user:
			login(request, user)
			return redirect('home')
		else:
			error = "Invalid username or password"
	return render(request, 'accounts/login.html', {'error': error})



def logout_view(request):
	logout(request)
	return redirect('logged_out')

def logged_out(request):
	return render(request, 'accounts/logged_out.html')


@login_required
def home(request):
	return render(request, 'accounts/home.html')
