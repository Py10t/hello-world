# Generated by Django 2.1.4 on 2019-03-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='Bestellung', max_length=250),
        ),
    ]