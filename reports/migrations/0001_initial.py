# Generated by Django 5.0.1 on 2024-03-31 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='material name')),
                ('url', models.URLField(max_length=128, verbose_name='url name')),
                ('is_approved', models.BooleanField(default=False, verbose_name='is approved')),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
            },
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.blockedresource')),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
            },
        ),
    ]