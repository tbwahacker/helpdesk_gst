from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket


# HOME PAGE
def index(request):
    return render(request, 'index.html')


# CREATE TICKET
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


# USER + STAFF DASHBOARD
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


# RESOLVE TICKET
@login_required
def resolve_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Only assigned staff can resolve
    if request.user == ticket.assigned_to:

        ticket.status = 'resolved'
        ticket.save()

        messages.success(request, 'Ticket resolved successfully.')

    return redirect('account')
