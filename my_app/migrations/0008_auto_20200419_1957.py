# Generated by Django 2.2.11 on 2020-04-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20200419_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
