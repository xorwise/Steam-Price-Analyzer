# Generated by Django 3.2.9 on 2021-11-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skin',
            name='highest_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='skin',
            name='lowest_price',
            field=models.FloatField(blank=True),
        ),
    ]
