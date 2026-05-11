from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket


def index(request):
    return render(request, 'index.html')

@login_required
def ticket(request):
    if request.method == 'POST':
        title = request.POST.get('issue')
        description = request.POST.get('description')
        priority = request.POST.get('priority')

        Ticket.objects.create(
            title=title,
            description=description,
            priority=priority,
            user=request.user
        )

        messages.success(request, "Ticket submitted successfully!")
        return redirect('account')

    return render(request, 'core_business/ticket.html')


@login_required
def account_view(request):

    # STAFF DASHBOARD
    if request.user.is_staff:

        tickets = Ticket.objects.filter(
            assigned_to=request.user
        ).order_by('-created_at')

        total_tickets = tickets.count()
        open_tickets = tickets.filter(status='open').count()
        resolved_tickets = tickets.filter(status='resolved').count()

        return render(request, 'staff/dashboard.html', {
            'tickets': tickets,
            'total_tickets': total_tickets,
            'open_tickets': open_tickets,
            'resolved_tickets': resolved_tickets
        })

    # NORMAL USER DASHBOARD
    else:

        tickets = Ticket.objects.filter(
            user=request.user
        ).order_by('-created_at')

        total_tickets = tickets.count()
        open_tickets = tickets.filter(status='open').count()
        resolved_tickets = tickets.filter(status='resolved').count()

        return render(request, 'user/dashboard.html', {
            'tickets': tickets,
            'total_tickets': total_tickets,
            'open_tickets': open_tickets,
            'resolved_tickets': resolved_tickets
        })