# Generated by Django 2.2.11 on 2020-04-25 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('fundacja', 'fundacja'), ('organizacja', 'organizacja pozarządowa'), ('zbiorka', 'zbiórka lokalna')], default='fundacja', max_length=100)),
                ('categories', models.ManyToManyField(to='my_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('phone_number', models.IntegerField()),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateField(auto_now=True)),
                ('pick_up_time', models.TimeField(auto_now=True)),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='my_app.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
