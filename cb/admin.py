from django.contrib import admin
from .models import BookMeta, Usr, Rps

# Register your models here.

admin.site.register(BookMeta)
admin.site.register(Usr)
admin.site.register(Rps)