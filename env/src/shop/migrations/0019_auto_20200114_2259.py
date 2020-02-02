# Generated by Django 3.0 on 2020-01-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200111_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinfo',
            name='from_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='to_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], null=True, unique=True),
        ),
    ]