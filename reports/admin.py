from django.contrib import admin
from .models import *


@admin.action(description="Подтвердить блокировку выбранных ресурсов")
def approve(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.register(BlockedResource)
class BlockedResourceAdmin(admin.ModelAdmin):
    search_fields = ['url']
    list_display = ['id', 'title', 'url']
    list_filter = ['is_approved']
    ordering = ('id', )
    actions = [approve]
