from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")


def logout_user(request):
    logout(request)
    return redirect('home')

