# Generated by Django 2.1.4 on 2019-03-19 17:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('amount', models.BigIntegerField()),
                ('order_date', models.DateField(default=datetime.date.today, verbose_name='Bestelldatum')),
                ('delivery_date', models.DateField(default=datetime.date.today, verbose_name='Lieferdatum')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Article')),
            ],
        ),
    ]
