# Generated by Django 4.2.11 on 2024-04-29 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_amigosdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigosdb',
            name='pending',
            field=models.BooleanField(null=True),
        ),
    ]