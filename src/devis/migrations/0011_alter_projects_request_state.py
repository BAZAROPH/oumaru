# Generated by Django 4.0.3 on 2022-04-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0010_remove_projects_client_projects_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='request_state',
            field=models.IntegerField(choices=[(0, 'En attente'), (1, 'Validé'), (2, 'Supprimé')], default=0),
        ),
    ]
