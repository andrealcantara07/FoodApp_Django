# Generated by Django 2.1 on 2019-01-31 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
