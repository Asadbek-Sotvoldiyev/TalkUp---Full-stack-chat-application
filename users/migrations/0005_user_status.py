# Generated by Django 5.1.6 on 2025-05-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='offline', max_length=10),
        ),
    ]
