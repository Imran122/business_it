# Generated by Django 3.2.5 on 2021-07-16 18:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('overview', models.TextField(max_length=400)),
                ('content', ckeditor.fields.RichTextField()),
                ('clients', models.CharField(blank=True, max_length=100, null=True)),
                ('clientsAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('projectUrl', models.CharField(blank=True, max_length=150, null=True)),
                ('projectGithub', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('postimage1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('postimage2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('postimage3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('file', models.FileField(null=True, upload_to='static/media')),
                ('is_published', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categorey')),
            ],
        ),
    ]
