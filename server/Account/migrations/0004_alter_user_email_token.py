# Generated by Django 5.0.1 on 2024-01-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_user_email_token_user_is_email_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
