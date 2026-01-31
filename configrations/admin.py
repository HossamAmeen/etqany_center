from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Logo, SuccessStory, Service, Advantage , Goal, Configuration


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'display_image', 'content_summary', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'title', 'content')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    display_image.short_description = _('image')

    def content_summary(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_summary.short_description = _('content')

admin.site.unregister(Group)

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ar', 'display_image', 'is_active', 'created_at')

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = _('image')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_summary', 'display_image', 'created_at')

    def description_summary(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description # noqa
    description_summary.short_description = _('description')

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = _('image')


@admin.register(Advantage )
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_summary', 'display_image', 'created_at')

    def description_summary(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description # noqa
    description_summary.short_description = _('description')

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = _('image')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_summary', 'display_image', 'created_at')

    def description_summary(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description # noqa
    description_summary.short_description = _('description')

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url)
        return "No Image"
    display_image.short_description = _('image')


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('certificate_image', 'certificate_description_summary', 'Our_message_summary', 'Our_vision_summary', 'created_at', 'email', 'phone_number', 'address', 'Technical_innovation_summary', 'Social_responsibility_summary', 'Customer_experience_summary') # noqa

    def certificate_description_summary(self, obj):
        return obj.certificate_description[:50] + '...' if len(obj.certificate_description) > 50 else obj.certificate_description # noqa
    certificate_description_summary.short_description = _('certificate_description')

    def Our_message_summary(self, obj):
        return obj.Our_message[:50] + '...' if len(obj.Our_message) > 50 else obj.Our_message # noqa
    Our_message_summary.short_description = _('Our message')

    def Our_vision_summary(self, obj):
        return obj.Our_vision[:50] + '...' if len(obj.Our_vision) > 50 else obj.Our_vision # noqa
    Our_vision_summary.short_description = _('Our vision')

    def Technical_innovation_summary(self, obj):
        return obj.Our_vision[:50] + '...' if len(obj.Our_vision) > 50 else obj.Our_vision # noqa
    Technical_innovation_summary.short_description = _('Technical innovation')
    def Social_responsibility_summary(self, obj):
        return obj.Social_responsibility[:50] + '...' if len(obj.Social_responsibility) > 50 else obj.Social_responsibility # noqa
    Social_responsibility_summary.short_description = _('Social responsibility')
    def Customer_experience_summary(self, obj):
        return obj.Customer_experience[:50] + '...' if len(obj.Customer_experience) > 50 else obj.Customer_experience # noqa
    Customer_experience_summary.short_description = _('Customer experience')
    def certificate_image(self, obj):
        if obj.certificate_image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.certificate_image.url)
        return "No Image"
    certificate_image.short_description = _('certificate_image')
