from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Message, MessageResponse, Profile

# registration of models into the admin page

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(MessageResponse)
admin.site.register(Profile)



