# Generated by Django 4.0.3 on 2022-04-20 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0003_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='user',
        ),
    ]
