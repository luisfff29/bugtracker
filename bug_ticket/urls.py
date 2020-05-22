from django.urls import path
from bug_ticket import views

urlpatterns = [
    path('', views.main, name='home'),
    path('ticket/<int:id>/', views.details, name='details'),
    path('ticket/submit/', views.create_ticket, name='submit'),
    path('ticket/invalid/', views.invalid_ticket, name='inv_tickets'),
    path('user/<str:name>/', views.user_profile, name='profile'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('action/<int:id>/', views.action, name='action'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view),
]
