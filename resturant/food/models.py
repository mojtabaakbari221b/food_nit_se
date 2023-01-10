from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils.html import mark_safe

class Category(models.Model):
    name = models.CharField(
        max_length=128,
    )

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name = models.CharField(
        max_length=256,
    )
    picture = models.ImageField(
        upload_to='food/images/',
        blank=False,
        null=False,
    )

    price = models.PositiveBigIntegerField()
    off_percent = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    location = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    time_to_deliver = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    def image_tag(self):
        return mark_safe(f'<img src="{self.picture.url}" width="150" height="150" />')
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
