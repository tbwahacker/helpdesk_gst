from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login, get_user_model
from django.contrib import messages

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff/dashboard.html')

def user_dashboard(request):
    return render(request, 'user/dashboard.html')

User = get_user_model()

def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Role-based redirect using Django built-in fields
            if user.is_superuser:
                return redirect('admin_dashboard')

            elif user.is_staff:
                return redirect('staff_dashboard')

            else:
                return redirect('user_dashboard')

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request, "User already exists")

        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            login(request, user)

            # New users go to user dashboard
            return redirect('user_dashboard')

    return render(request, 'authentication/signup.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')