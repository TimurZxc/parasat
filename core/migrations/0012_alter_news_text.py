# Generated by Django 4.2.7 on 2024-04-30 10:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_comment_text_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
