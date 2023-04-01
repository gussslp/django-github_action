from django.contrib import admin
from .models import Post,Video,Audio

admin.site.register(Post)
admin.site.register(Audio)
admin.site.register(Video)