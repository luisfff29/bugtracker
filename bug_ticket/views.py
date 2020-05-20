from django.shortcuts import render, reverse
from bug_ticket.forms import CreateTicket
from bug_ticket.models import Author, Ticket

from django.http import HttpResponseRedirect


# Create your views here.
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


def user_profile(request, name):
    return render(request, 'profile.html')


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


def invalid_ticket(request):
    invalid = Ticket.objects.filter(status='Invalid')
    return render(request, 'invalid_ticket.html', {'invalid': invalid})


def details(request, id):
    data = Ticket.objects.get(id=id)
    return render(request, 'details.html', {'data': data})


def edit(request, id):
    return render(request, 'edit.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')
