# Generated by Django 3.1 on 2020-08-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0013_auto_20200822_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectures',
            name='sub',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Maths', 'Maths')], max_length=200, null=True),
        ),
    ]
