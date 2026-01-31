from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class SuccessStory(models.Model):
    name = models.CharField(_("name"), max_length=100)
    name_ar = models.CharField(_("name_ar"), max_length=100, null=True, blank=True)
    title = models.CharField(_("title"), max_length=150, blank=True)
    title_ar = models.CharField(_("title_ar"), max_length=150, blank=True)
    content = models.TextField(_("content"))
    content_ar = models.TextField(_("content_ar"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to='success_stories/', blank=True, null=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Success Story")
        verbose_name_plural = _("Success Stories")


class Logo(models.Model):
    image = models.ImageField(_("image"))
    name = models.CharField(_("name"), max_length=100)
    name_ar = models.CharField(_("name_ar"), max_length=100, null=True, blank=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Logo")
        verbose_name_plural = _("Logos")


class Service(models.Model):
    title = models.CharField(_("title"), max_length=200, blank=True)
    title_ar = models.CharField(_("title_ar"),
                                max_length=200, null=True, blank=True)
    description = models.TextField(_("description"), blank=True)
    description_ar = models.TextField(_("description_ar"),
                                      null=True, blank=True)
    image = models.ImageField(upload_to='services/icons/',
                              null=True, blank=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class WhyChooseUs(models.Model):
    title = models.CharField(_("title"), max_length=200, blank=True)
    title_ar = models.CharField(_("title_ar"),
                                max_length=200, null=True, blank=True)
    description = models.TextField(_("description"), blank=True)
    description_ar = models.TextField(_("description_ar"),
                                      null=True, blank=True)
    image = models.ImageField(upload_to='why_choose_us/icons/',
                              null=True, blank=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Why Choose Us")
        verbose_name_plural = _("Why Choose Us")
