from django.db import models
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify


class BlockedResource(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('material name'))
    url = models.URLField(max_length=128, blank=True, null=True, verbose_name=_('url name'))
    is_approved = models.BooleanField(default=False,  verbose_name=_('is approved'))

    class Meta:
        verbose_name = _('report')
        verbose_name_plural = _('reports')


class ReportItem(models.Model):
    time = models.TimeField(auto_now=True)
    resource = models.ForeignKey(BlockedResource, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def is_actual(self):
        return not self.resource.is_approved

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('report')
        verbose_name_plural = _('reports')
