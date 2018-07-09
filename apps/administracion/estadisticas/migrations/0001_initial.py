# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provedor', models.CharField(max_length=30)),
                ('peso', models.DecimalField(decimal_places=3, max_digits=5)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.CharField(max_length=100)),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Descargas',
                'verbose_name': 'Descarga',
            },
        ),
        migrations.CreateModel(
            name='RegistroCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_id', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('login', models.CharField(max_length=30)),
                ('coins_compradas', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('fecha_compra', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Registro Compras',
                'verbose_name': 'Registro Compra',
            },
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField()),
                ('name', models.CharField(max_length=26)),
                ('guild_name', models.CharField(max_length=26, null=True)),
                ('level', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('ranking', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
