from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import Logo, SuccessStory, service


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'display_image', 'content_summary', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'title', 'content')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'

    def content_summary(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_summary.short_description = 'Content'

admin.site.unregister(Group)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'


@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_summary', 'display_image')

    def description_summary(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description # noqa
    description_summary.short_description = 'Description'

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'
