# Generated by Django 2.0.3 on 2019-04-07 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.CharField(max_length=120)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password_hash', models.CharField(max_length=60)),
                ('locations', models.ManyToManyField(through='users.UserLocations', to='locations.Locations')),
            ],
        ),
        migrations.AddField(
            model_name='userlocations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]
