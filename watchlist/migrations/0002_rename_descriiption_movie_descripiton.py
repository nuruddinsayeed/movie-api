# Generated by Django 3.2.7 on 2021-09-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='descriiption',
            new_name='descripiton',
        ),
    ]
