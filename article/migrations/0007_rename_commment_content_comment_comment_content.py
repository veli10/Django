# Generated by Django 5.0.6 on 2024-06-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commment_content',
            new_name='comment_content',
        ),
    ]