# Generated by Django 2.2.4 on 2021-05-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_user_password1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
