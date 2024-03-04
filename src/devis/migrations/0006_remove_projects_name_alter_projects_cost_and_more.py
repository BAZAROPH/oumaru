# Generated by Django 4.0.3 on 2022-04-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0005_clients_address_clients_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='name',
        ),
        migrations.AlterField(
            model_name='projects',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Coût'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='delay',
            field=models.DateField(verbose_name='Délai de livraison'),
        ),
    ]
