# Generated by Django 3.0.6 on 2020-07-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thoughts',
            field=models.TextField(default=None, null=True),
        ),
    ]
