# Generated by Django 3.1.5 on 2021-01-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('upload_locn', models.ImageField(upload_to='maps/')),
                ('user', models.CharField(max_length=50)),
                ('geofence_locn', models.ImageField(upload_to='geofenced_maps/')),
            ],
        ),
    ]
