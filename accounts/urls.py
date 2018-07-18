from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/',views.LoginView.as_view(), name='login'),
    path('accounts/profile/',views.ProfileView.as_view(), name='profile'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
]