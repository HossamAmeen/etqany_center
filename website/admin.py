from django.contrib import admin

from .models import CustomerExperience, SuccessStory, Vision

admin.site.register(SuccessStory)
admin.site.register(Vision)
admin.site.register(CustomerExperience)
