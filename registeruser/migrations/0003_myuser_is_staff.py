# Generated by Django 4.0.2 on 2022-02-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeruser', '0002_remove_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
