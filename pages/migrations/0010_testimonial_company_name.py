# Generated by Django 3.2.5 on 2021-08-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_testimonial_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]