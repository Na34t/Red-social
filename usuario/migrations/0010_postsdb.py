# Generated by Django 4.2.11 on 2024-04-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_alter_amigosdb_pending'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=40)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]