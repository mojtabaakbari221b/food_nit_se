# Generated by Django 3.2.4 on 2023-01-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='foods',
        ),
        migrations.DeleteModel(
            name='CartFood',
        ),
    ]
