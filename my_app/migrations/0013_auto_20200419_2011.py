# Generated by Django 2.2.11 on 2020-04-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_auto_20200419_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(null=True),
        ),
    ]