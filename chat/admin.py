from django.contrib import admin
from .models import ChatGroup, Message

admin.site.register([ChatGroup, Message])
