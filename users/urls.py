from django.urls import path
from .views import RegisterView, logout_user, UpdateProfileView, UpdateProfilePhotoView

app_name = 'users'

urlpatterns = [
    path('signin/', RegisterView.as_view(), name='register'),
    path('sign-out/', logout_user, name='logout_user'),
    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('update-photo/', UpdateProfilePhotoView.as_view(), name='update_photo'),
]