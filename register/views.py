from django.shortcuts import render, redirect
from .forms import RegisterForm
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
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('') # replace 'home' with the URL of your app's home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
