# Generated by Django 5.0.6 on 2024-06-04 16:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Mezmun'),
        ),
    ]
