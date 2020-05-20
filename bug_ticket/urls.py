from django.urls import path
from bug_ticket import views

urlpatterns = [
    path('', views.main),
    path('ticket/<int:id>/', views.details, name='details'),
    path('ticket/submit/', views.create_ticket),
    path('ticket/invalid/', views.invalid_ticket),
    path('user/<str:name>/', views.user_profile),
    path('edit/<int:id>/', views.edit),
    path('login/', views.login_view),
    path('signup/', views.signup_view),
]
