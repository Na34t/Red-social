# Generated by Django 4.2.11 on 2024-04-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_amigosdb_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigosdb',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]
