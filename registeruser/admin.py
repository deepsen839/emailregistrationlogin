from django.contrib import admin
from .models import myUser
# Register your models here.
@admin.register(myUser)
class myUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','email',)

