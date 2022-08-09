from django.contrib import admin
from .models import Topic,Room,Reply,Profile,Message,Notification,Latest

# Register your models here.
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Reply)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Latest)