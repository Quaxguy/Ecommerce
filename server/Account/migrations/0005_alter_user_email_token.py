# Generated by Django 5.0.1 on 2024-01-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_email_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
