from django import forms
from bug_ticket.models import Author, Ticket


class CreateTicket(forms.ModelForm):
    class Meta():
        model = Ticket
        fields = ['title', 'description']


class UpdateTicket(forms.ModelForm):
    class Meta():
        model = Ticket
        fields = ['title', 'description', 'user_assigned', 'user_completed']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())
