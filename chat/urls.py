from django.urls import path
from .views import ChatView, ChatDirectView

urlpatterns = [
    path('', ChatView.as_view(), name='home'),
    path('chat-group/<int:id>/', ChatDirectView.as_view(), name='chat_group'),
]