from django.contrib import admin
from .models import User, Transfer, Document

# Register your models here.
admin.site.register(User)
admin.site.register(Transfer)
admin.site.register(Document)
