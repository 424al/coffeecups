# Generated by Django 3.0 on 2019-12-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20191211_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinfo',
            name='embed_id',
            field=models.CharField(help_text='USE "+" SYMBOLS INSTEAD OF SPACE', max_length=200, null=True),
        ),
    ]
