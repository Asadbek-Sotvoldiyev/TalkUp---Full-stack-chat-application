from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from users.models import User
from .models import ChatGroup, Message


class ChatView(LoginRequiredMixin, View):
    login_url = "/users/signin"
    redirect_field_name = None

    def get(self, request):
        # chatgroups = ChatGroup.objects.filter(users=request.user).prefetch_related("users"
        chatgroups = ChatGroup.objects.all()


        chat_users = set()

        for group in chatgroups:
            others = group.users.exclude(id=request.user.id)
            for user in others:
                chat_users.add(user)

        data = {
            "chat_users": chat_users
        }

        return render(request, 'chat/index.html', data)

class ChatDirectView(LoginRequiredMixin, View):
    login_url = "/users/signin"
    redirect_field_name = None

    def get(self, request, id):
        # chatgroups = ChatGroup.objects.filter(users=request.user).prefetch_related("users")
        chatgroups = ChatGroup.objects.all()
        to_user = User.objects.get(id=id)
        chat_group = ChatGroup.objects.filter(users=request.user).filter(users=to_user).first()

        chat_users = set()
        for group in chatgroups:
            others = group.users.exclude(id=request.user.id)
            for user in others:
                chat_users.add(user)

        global messages
        if chat_group:
            messages = Message.objects.filter(chatgroup=chat_group)
        else:
            chat_group = ChatGroup.objects.create(name=f"{to_user.username}_with_{request.user.username}")
            chat_group.users.add(to_user, request.user)

        data = {
            "chat_users": chat_users,
            "messages": messages,
            "chat_group": chat_group,
            "to_user": to_user
        }

        return render(request, 'chat/chat_direct.html', data)
    
    
