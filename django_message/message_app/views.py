from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants as message_constants  # ✅ NEW

def home(request):
    return render(request, "message_app/home.html")


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name == "":
            messages.error(request, "Name cannot be empty ❌")
            return redirect("home")

        if len(name) < 3:
            messages.warning(request, "Name is too short (min 3 characters) ⚠️")
            return redirect("home")

        if name.lower() == "admin":
            messages.info(request, "You entered a reserved keyword (admin) ℹ️")

        messages.success(request, f"Hello {name}! Form submitted successfully ✅")
        return redirect("home")

    messages.info(request, "Please submit the form correctly ℹ️")
    return redirect("home")


# ✅ Buttons for testing
def msg_success(request):
    messages.success(request, "Bootstrap Success Alert ✅")
    return redirect("home")

def msg_error(request):
    messages.error(request, "Bootstrap Error Alert ❌")
    return redirect("home")

def msg_warning(request):
    messages.warning(request, "Bootstrap Warning Alert ⚠️")
    return redirect("home")

def msg_info(request):
    messages.info(request, "Bootstrap Info Alert ℹ️")
    return redirect("home")


# ✅ NEW: add_message() demo
def msg_add_message(request):
    messages.add_message(
        request,
        message_constants.SUCCESS,
        "Success using add_message ✅"
    )
    return redirect("home")
