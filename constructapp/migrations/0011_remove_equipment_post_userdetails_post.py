# Generated by Django 5.0.3 on 2024-03-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0010_equipment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='post',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='post',
            field=models.CharField(default='', max_length=75),
        ),
    ]