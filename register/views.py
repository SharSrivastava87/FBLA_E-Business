from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            return redirect('Homepage:RoomList')

    else:
        form = AuthenticationForm()
    return render(request, 'LoginPage.html', {'form':form})
