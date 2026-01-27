from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
