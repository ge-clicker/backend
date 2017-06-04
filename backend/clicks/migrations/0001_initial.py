# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 14:03
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClickRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.IntegerField()),
                ('ip_address', models.GenericIPAddressField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('primary_color', colorfield.fields.ColorField(max_length=18)),
                ('secondary_color', colorfield.fields.ColorField(blank=True, max_length=18, null=True)),
                ('image', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='clickrecord',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='clicks.Party'),
        ),
    ]
