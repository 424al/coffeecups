# Generated by Django 3.0 on 2019-12-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=2000)),
                ('contact', models.TextField(max_length=2000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
