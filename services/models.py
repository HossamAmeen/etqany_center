from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    image = models.ImageField(_("Image"), upload_to="services/")
    brief = models.TextField(_("Brief"), max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title
