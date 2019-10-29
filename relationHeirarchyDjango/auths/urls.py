from django.urls import path
from . import views as auths_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'auths'

urlpatterns = [
    path('register/', auths_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="auths/login.html", extra_context={'activate':'login'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auths/logout.html"), name='logout'),
    # path('logout/', auth_views.logout, name="logout"),
    
]
