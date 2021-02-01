# Generated by Django 3.1.5 on 2021-01-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210130_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fieldofactivity',
            field=models.ManyToManyField(related_name='user', to='profiles.FieldOfActivity'),
        ),
    ]