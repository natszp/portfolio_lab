# Generated by Django 2.2.11 on 2020-04-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_auto_20200419_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (2, 'No'), (3, '')]),
        ),
    ]