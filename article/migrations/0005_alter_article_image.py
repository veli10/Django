# Generated by Django 5.0.6 on 2024-06-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Article images', verbose_name='Image'),
        ),
    ]
