# Generated by Django 3.0 on 2019-12-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20191223_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopinfo',
            old_name='featured',
            new_name='status',
        ),
    ]
