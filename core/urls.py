from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('frontpage/', views.frontpage, name='frontpage'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
