from django.urls import path
from bug_ticket import views

urlpatterns = [
    path('', views.main),
    path('ticket/<int:id>/', views.details),
    path('user/<str:name>/', views.user_profile),
    path('edit/<int:id>/', views.edit),
    path('login/', views.login_view),
    path('signup/', views.signup_view),
]
