# Generated by Django 4.2.7 on 2024-04-30 10:54

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]