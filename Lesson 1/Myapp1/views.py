from django.shortcuts import render, redirect
from .forms import SimpleForm

def simple_form_view(request):
    form = SimpleForm()

    if request.method == "POST":
        form = SimpleForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            print(username, email, password)  # just for testing

            return redirect('login')

    return render(request, 'Myapp1/register.html', {'form': form})



from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    error = ""

    # Demo user (hardcoded)
    demo_user = {
        'username': 'ishu',
        'password': '12345',
        'email': 'ishu@gmail.com'
    }

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username == demo_user['username'] and password == demo_user['password']:
                return render(request, 'Myapp1/success.html', {
                    'username': username,
                    'email': demo_user['email']
                })
            else:
                error = "Invalid username or password"

    return render(request, 'Myapp1/login.html', {'form': form, 'error': error})



