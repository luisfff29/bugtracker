from django.shortcuts import render, reverse
from bug_ticket.forms import CreateTicket
from bug_ticket.models import Author, Ticket

from django.http import HttpResponseRedirect


# Create your views here.
def main(request):
    return render(request, 'main.html')


def user_profile(request, name):
    return render(request, 'profile.html')


def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            t = Ticket.objects.create(
                title=data['title'], description=data['description'], user_filed=Author.objects.get(username=request.user.username))
        return HttpResponseRedirect(reverse('details', args=(t.id, )))

    form = CreateTicket()
    return render(request, 'create_ticket.html', {'form': form})


def invalid_ticket(request):
    return render(request, 'invalid_ticket.html')


def details(request, id):
    return render(request, 'details.html')


def edit(request, id):
    return render(request, 'edit.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')
