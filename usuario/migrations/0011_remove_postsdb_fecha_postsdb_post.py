# Generated by Django 4.2.11 on 2024-05-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_postsdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsdb',
            name='fecha',
        ),
        migrations.AddField(
            model_name='postsdb',
            name='post',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
