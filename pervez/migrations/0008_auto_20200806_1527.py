# Generated by Django 3.0.8 on 2020-08-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0007_lectures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='sub_topic',
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic', models.CharField(blank=True, max_length=200, null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pervez.Lectures')),
            ],
        ),
    ]
