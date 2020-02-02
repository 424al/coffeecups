# Generated by Django 3.0 on 2020-01-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200114_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopinfo',
            name='from_hour',
        ),
        migrations.RemoveField(
            model_name='shopinfo',
            name='to_hour',
        ),
        migrations.RemoveField(
            model_name='shopinfo',
            name='weekday',
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='friday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='monday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='saturday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='source',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='sunday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='thursday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='tuesday',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='wednesday',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
