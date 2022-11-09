from django.contrib import admin
from .models import Message, Like

class MessageAdmin(admin.ModelAdmin):
    list_display = ['pub_date','message_text']
    search_fields = ('pub_date','message_text')

class LikeAdmin(admin.ModelAdmin):
    list_display = ['message','like']
    search_fields = ('message', 'like')

admin.site.register(Message, MessageAdmin)
admin.site.register(Like, LikeAdmin)

