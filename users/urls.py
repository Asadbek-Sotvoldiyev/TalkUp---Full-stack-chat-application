from django.urls import path
from .views import RegisterView, logout_user

app_name = 'users'

urlpatterns = [
    path('signin/', RegisterView.as_view(), name='register'),
    path('sign-out/', logout_user, name='logout_user'),
]