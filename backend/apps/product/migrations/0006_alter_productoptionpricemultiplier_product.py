# Generated by Django 4.0.7 on 2022-11-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_productclassoptiongroup_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoptionpricemultiplier',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multipliers', to='product.product'),
        ),
    ]
