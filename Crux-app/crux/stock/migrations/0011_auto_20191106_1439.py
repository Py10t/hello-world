# Generated by Django 2.2.7 on 2019-11-06 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20191106_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stock.Article'),
        ),
    ]