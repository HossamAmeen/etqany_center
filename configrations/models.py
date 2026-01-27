from django.db import models
from django.utils.translation import gettext_lazy as _

class SuccessStory(models.Model):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=150, blank=True)
    title_ar = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    content_ar = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='success_stories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Success Story")
        verbose_name_plural = _("Success Stories")