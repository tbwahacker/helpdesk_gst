from django.shortcuts import render

def login(request):
    return render(request, 'authentication/login.html')

def signup(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return
    # return render(request, 'authentication/login.html')
