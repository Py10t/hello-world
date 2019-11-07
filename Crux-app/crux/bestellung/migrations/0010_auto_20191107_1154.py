# Generated by Django 2.2.7 on 2019-11-07 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0009_auto_20191107_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Lieferdatum'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Bestelldatum'),
        ),
    ]
