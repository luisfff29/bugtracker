from django.urls import path
from bug_ticket import views

urlpatterns = [
    path('', views.main),
]
