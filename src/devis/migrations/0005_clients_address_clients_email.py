# Generated by Django 4.0.3 on 2022-04-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0004_remove_clients_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
    ]
