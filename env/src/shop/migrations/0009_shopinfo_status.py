# Generated by Django 3.0 on 2019-12-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20191211_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinfo',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
