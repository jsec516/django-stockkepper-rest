# Generated by Django 2.0 on 2018-01-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='allocated_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
