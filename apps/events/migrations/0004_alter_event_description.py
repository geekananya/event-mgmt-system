# Generated by Django 5.0.9 on 2024-11-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
