# Generated by Django 2.2.6 on 2019-10-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20191013_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuatormeasurement',
            name='token',
            field=models.CharField(default='81293812', max_length=30),
        ),
    ]