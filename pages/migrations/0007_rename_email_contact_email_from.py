# Generated by Django 3.2.5 on 2021-08-10 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='email_from',
        ),
    ]
