from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Donation)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Institution)
class AuthorAdmin(admin.ModelAdmin):
    pass
