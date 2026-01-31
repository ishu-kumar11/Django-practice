from django.shortcuts import render, redirect
from .forms import UserLocationForm

def location_form(request):
    if request.method == "POST":
        form = UserLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = UserLocationForm()

    return render(request, "map_app/location_form.html", {"form": form})


def success_page(request):
    return render(request, "map_app/success.html")
