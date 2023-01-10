from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from resturant.cart.models import Cart
from . import model_fields
from .managers import UserManager


class User(AbstractUser):
    objects = UserManager()
    
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

    def get_my_cart(self):
        return Cart.objects.get_my_cart(self)

User._meta.get_field('username').editable = False
User._meta.get_field('username').blank = True
User._meta.get_field('username').null = True
