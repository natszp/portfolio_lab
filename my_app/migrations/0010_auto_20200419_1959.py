# Generated by Django 2.2.11 on 2020-04-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20200419_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=1),
        ),
    ]
