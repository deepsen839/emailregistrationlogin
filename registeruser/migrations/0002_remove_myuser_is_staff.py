# Generated by Django 4.0.2 on 2022-02-04 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeruser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
    ]
