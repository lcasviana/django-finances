# Generated by Django 3.2.4 on 2021-06-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapagar',
            name='data_pagamento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contareceber',
            name='data_recebimento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]