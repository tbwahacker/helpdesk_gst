# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from authentication.decorators import admin_required, staff_required
from django.contrib.auth.decorators import login_required


@login_required
@admin_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
@staff_required
def staff_dashboard(request):
    return render(request, 'staff/dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'user/dashboard.html')

User=get_user_model()

def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:

            login(request, user)

            # 🔥 Role-based redirect
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'staff':
                return redirect('staff_dashboard')
            else:
                return redirect('user_dashboard')

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST.get('role')

        if not role:
            messages.error(request, "Please select a role")
            return redirect('signup')

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
            user.save()

            login(request, user)

            # ✅ Optional: role-based redirect
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'staff':
                return redirect('staff_dashboard')
            else:
                return redirect('user_dashboard')

    return render(request, 'authentication/signup.html')



def logout_view(request):  # renamed from 'logout'
    auth_logout(request)
    return redirect('login')  # or 'index' if you prefer
