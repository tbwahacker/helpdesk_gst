# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User=get_user_model()

def login_view(request):  # renamed from 'login' to avoid conflict
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            # This is the line that sends you to the account page
            print(f"user: {user}")
            login(request, user)
            return redirect('account')
        else:
            print("Invalid username or password. Please try again.")
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', )


def signup(request):
    # Keep your signup logic here (or update it later)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = User.objects.filter(username=username).first()

        if user:
            print("User already exists")
            messages.error(request, "User already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('account')


    return render(request, 'authentication/signup.html')


def logout_view(request):  # renamed from 'logout'
    auth_logout(request)
    return redirect('login')  # or 'index' if you prefer
