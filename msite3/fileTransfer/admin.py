from django.contrib import admin
from .models import UserProfile, Document #chnge back to User if RIP

# Register your models here.
admin.site.register(UserProfile) #changed this, from User to UserProfile
admin.site.register(Document)
