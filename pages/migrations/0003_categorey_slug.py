# Generated by Django 3.2.5 on 2021-07-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_works_projectdelevery'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorey',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
