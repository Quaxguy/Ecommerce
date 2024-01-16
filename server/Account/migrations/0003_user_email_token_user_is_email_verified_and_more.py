# Generated by Django 5.0.1 on 2024-01-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_remove_user_name_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]