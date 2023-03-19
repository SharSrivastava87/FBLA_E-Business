from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage:login')
        else:
            if form.errors.get('password') and 'Passwords do not match' in form.errors['password']:
                error_msg = 'Passwords do not match. Please try again.'
            else:
                error_msg = 'Form is invalid. Please correct the errors below.'
            return render(response, "register.html", {"form": form, "error_msg": error_msg})
    else:
        form = RegisterForm()
        return render(response, "register.html", {"form": form})




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('Homepage:RoomList')

    else:
        form = AuthenticationForm()
    return render(request, 'LoginPage.html', {'form':form})
