# Generated by Django 2.2.7 on 2019-11-26 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maschinenplanung', '0004_auto_20191126_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auftragsobjekt',
            name='latest_finish',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Lieferdatum'),
        ),
    ]
