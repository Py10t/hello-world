# Generated by Django 2.2.7 on 2019-11-06 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0009_auto_20190427_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktuelles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Article')),
                ('stock_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stock.Article')),
            ],
        ),
    ]
