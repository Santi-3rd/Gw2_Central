# Generated by Django 4.2.4 on 2023-10-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_user',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='app_user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
