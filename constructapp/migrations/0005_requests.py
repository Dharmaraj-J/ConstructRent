# Generated by Django 4.1.7 on 2024-03-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0004_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=75)),
                ('customer_village', models.CharField(default='', max_length=75)),
                ('customer_taluka', models.CharField(default='', max_length=75)),
                ('customer_phone', models.CharField(default='', max_length=75)),
                ('equipment_name', models.CharField(default='', max_length=75)),
                ('equipment_id', models.IntegerField(null=True)),
                ('equipment_holder_phone_no', models.IntegerField(null=True)),
                ('rent', models.IntegerField(null=True)),
                ('take_date', models.CharField(default='', max_length=75)),
                ('give_date', models.CharField(default='', max_length=75)),
                ('total_rent', models.IntegerField(null=True)),
            ],
        ),
    ]