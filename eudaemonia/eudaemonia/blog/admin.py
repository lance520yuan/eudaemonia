from django.contrib import admin

from .models import *

admin.site.register(Article)
admin.site.register(Website)
admin.site.register(User)
admin.site.register(Commit)