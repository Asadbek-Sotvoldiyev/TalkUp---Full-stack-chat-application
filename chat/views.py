from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class ChatView(LoginRequiredMixin, View):
    login_url = "/users/signin"
    redirect_field_name = None
    def get(self, request):
        return render(request, 'chat/index.html')
