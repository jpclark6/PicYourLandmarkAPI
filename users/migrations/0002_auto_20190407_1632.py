# Generated by Django 2.0.3 on 2019-04-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlocations',
            old_name='location',
            new_name='locations',
        ),
        migrations.RenameField(
            model_name='userlocations',
            old_name='user',
            new_name='users',
        ),
    ]
