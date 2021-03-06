# Generated by Django 2.0 on 2018-01-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180113_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocateditem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_allocations', to='webapp.Product'),
            preserve_default=False,
        ),
    ]
