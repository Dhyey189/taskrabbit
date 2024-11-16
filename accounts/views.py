from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import ProfileForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout as logout_method
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    """
    Signup view to handle user registration algon with validations.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/home/')

    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def login_view(request):
    """
    Login view to handle user session with validations.
    """
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect("/accounts/home/", context = {"message": message})
            else:
                message = 'Login failed!'
    

    return render(request, "login.html", {"form": form})

def home(request):
    return render(request, "home.html")

def logout(request):
    """
    Logout view to end user session.
    """
    logout_method(request)

    return redirect('/accounts/home/')


def profile(request):
    """
    View to handle User profile updation (in progress)
    """
    form = ProfileForm()
    if request.method == "PUT":

        form = ProfileForm(request.PUT, request.FILES)

        # Getting the current instance object to display in the template  
        User.objects.filter(id=request.user.id).update(**form.data)
            
        return render(request, 'profile.html', {'form': form})

    return render(request, 'profile.html', {'form': form})  
