# Generated by Django 4.2.11 on 2024-04-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_alter_amigosdb_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigosdb',
            name='pending',
            field=models.CharField(max_length=1),
        ),
    ]
