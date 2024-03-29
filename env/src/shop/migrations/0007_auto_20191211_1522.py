# Generated by Django 3.0 on 2019-12-11 15:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_shopinfo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinfo',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='address',
            field=models.TextField(max_length=75, null=True),
        ),
    ]
