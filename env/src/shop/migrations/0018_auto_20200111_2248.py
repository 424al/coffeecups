# Generated by Django 3.0 on 2020-01-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200111_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopinfo',
            name='bio',
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='about2',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='about',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
