from django.contrib import admin
from bug_ticket.models import Author, Ticket
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Author, UserAdmin)
admin.site.register(Ticket)
