# Generated by Django 3.0.8 on 2020-08-07 11:24

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0011_delete_subtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic', models.CharField(blank=True, max_length=200, null=True)),
                ('vedio', embed_video.fields.EmbedVideoField(null=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pervez.Lectures')),
            ],
        ),
    ]
