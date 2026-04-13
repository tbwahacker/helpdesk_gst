from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ticket(request):
    return render(request, 'core_business/ticket.html')
