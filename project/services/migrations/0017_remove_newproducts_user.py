# Generated by Django 5.0.1 on 2024-05-14 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_newproducts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newproducts',
            name='user',
        ),
    ]