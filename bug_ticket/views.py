from django.shortcuts import render, reverse
from bug_ticket.forms import CreateTicket, UpdateTicket, LoginForm, CreateAuthor
from bug_ticket.models import Author, Ticket
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url='/login/')
def main(request):
    new = Ticket.objects.filter(status='New')
    inprogress = Ticket.objects.filter(status='In Progress')
    done = Ticket.objects.filter(status='Done')
    data = {
        'new': new,
        'inprogress': inprogress,
        'done': done
    }
    return render(request, 'main.html', context=data)


@login_required(login_url='/login/')
def user_profile(request, name):
    filed = Ticket.objects.filter(
        status='New', user_filed=Author.objects.get(username=name))
    assigned = Ticket.objects.filter(
        user_assigned=Author.objects.get(username=name))
    completed = Ticket.objects.filter(
        status='Done',
        user_completed=Author.objects.get(username=name))
    usr = Author.objects.get(username=name)
    len_tickets_reported = len(Ticket.objects.filter(user_filed=usr))
    data = {
        'filed': filed,
        'assigned': assigned,
        'completed': completed,
        'usr': usr,
        'num': len_tickets_reported
    }
    return render(request, 'profile.html', context=data)


@login_required(login_url='/login/')
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            t = Ticket.objects.create(
                title=data['title'], description=data['description'], status='New', user_filed=Author.objects.get(username=request.user.username))
        return HttpResponseRedirect(reverse('details', args=(t.id, )))

    form = CreateTicket()
    return render(request, 'create_ticket.html', {'form': form})


@login_required(login_url='/login/')
def invalid_ticket(request):
    invalid = Ticket.objects.filter(status='Invalid')
    return render(request, 'invalid_ticket.html', {'invalid': invalid})


@login_required(login_url='/login/')
def details(request, id):
    data = Ticket.objects.get(id=id)
    return render(request, 'details.html', {'data': data})


@login_required(login_url='/login/')
def edit(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = UpdateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.status = 'New'
            if data['user_assigned']:
                ticket.status = 'In Progress'
                ticket.user_assigned = data['user_assigned']
                ticket.user_completed = None
            if data['user_completed']:
                ticket.status = 'Done'
                ticket.user_assigned = None
                ticket.user_completed = data['user_completed']
            ticket.save()
        return HttpResponseRedirect(reverse('details', args=(id, )))

    form = UpdateTicket(initial={
        'title': ticket.title,
        'description': ticket.description,
        'user_assigned': ticket.user_assigned,
        'user_completed': ticket.user_completed,
    })
    return render(request, 'edit.html', {'form': form})


@login_required(login_url='/login/')
def action(request, id):
    value = request.GET['value']
    ticket = Ticket.objects.get(id=id)
    if value == 'assign':
        ticket.status = 'In Progress'
        ticket.user_assigned = Author.objects.get(
            username=request.user.username)
        ticket.save()
        return HttpResponseRedirect(reverse('details', args=(id, )))
    if value == 'unassign':
        ticket.status = 'New'
        ticket.user_assigned = None
        ticket.user_completed = None
        ticket.save()
        return HttpResponseRedirect(reverse('details', args=(id, )))
    if value == 'done':
        ticket.status = 'Done'
        ticket.user_assigned = None
        ticket.user_completed = Author.objects.get(
            username=request.user.username)
        ticket.save()
        return HttpResponseRedirect(reverse('details', args=(id, )))
    if value == 'invalid':
        ticket.status = 'Invalid'
        ticket.user_assigned = None
        ticket.user_completed = None
        ticket.save()
        return HttpResponseRedirect(reverse('details', args=(id, )))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = authenticate(
                request, username=data['username'], password=data['password'])
            if usuario:
                login(request, usuario)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def signup_view(request):
    if request.method == 'POST':
        form = CreateAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create_user(
                username=data['username'],
                password=data['password'],
                is_staff=data['is_staff'],
                is_superuser=data['is_superuser']
            )
        return HttpResponseRedirect(reverse('login'))

    form = CreateAuthor()
    return render(request, 'signup.html', {'form': form})
