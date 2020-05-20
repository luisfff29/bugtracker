from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main.html')


def user_profile(request, name):
    return render(request, 'profile.html')


def details(request, id):
    return render(request, 'details.html')


def edit(request, id):
    return render(request, 'edit.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')
