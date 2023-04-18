# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment', models.CharField(choices=[('1x', '1x'), ('2x', '2x'), ('3x', '3x'), ('4x', '4x'), ('5x', '5x'), ('6x', '6x')], default='1x', max_length=2)),
                ('discount_or_increase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('installment_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PaymentRegister'),
        ),
    ]