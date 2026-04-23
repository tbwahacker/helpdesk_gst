
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ticket(request):
    return render(request, 'core_business/ticket.html')

@login_required
def account_view(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account.html', context)