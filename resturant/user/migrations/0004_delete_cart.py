# Generated by Django 4.1.5 on 2023-01-10 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
