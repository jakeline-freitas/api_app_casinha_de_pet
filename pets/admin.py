from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "type",
        "city",
        "vacinne",
        "owner",
        "photo"
        ]
