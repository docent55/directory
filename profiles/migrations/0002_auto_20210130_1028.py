# Generated by Django 3.1.5 on 2021-01-30 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='telephone_number',
            new_name='phone_number',
        ),
    ]
