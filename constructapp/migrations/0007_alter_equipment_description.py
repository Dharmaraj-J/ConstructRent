# Generated by Django 5.0.3 on 2024-03-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0006_requests_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(default=''),
        ),
    ]