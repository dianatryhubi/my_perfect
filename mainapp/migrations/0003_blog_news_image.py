# Generated by Django 2.1.5 on 2019-02-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190204_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
