from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Device(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='devices', verbose_name=_('User')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at')
    )

    def __str__(self):
        return self.name
