from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from . import model_fields

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = model_fields.LowercaseEmailField(
        _('email address'),
        unique=True,
        blank=False,
        null=False,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    name = models.CharField(
        _("name"),
        max_length=150,
        blank=False,
    )

