# Generated by Django 3.1 on 2020-08-25 08:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0029_remove_subtopic_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='extras',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
