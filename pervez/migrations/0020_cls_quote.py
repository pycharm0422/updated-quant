# Generated by Django 3.1 on 2020-08-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0019_auto_20200822_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='cls',
            name='quote',
            field=models.TextField(blank=True, null=True),
        ),
    ]
