from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main.html')


def user_profile(request, name):
    return render(request, 'profile.html')


def create_ticket(request):
    return render(request, 'create_ticket.html')


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
