from django import forms
from bug_ticket.models import Author, Ticket


class CreateTicket(forms.ModelForm):
    class Meta():
        model = Ticket
        fields = ['title', 'description']
