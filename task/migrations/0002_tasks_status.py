# Generated by Django 5.1.1 on 2024-10-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
