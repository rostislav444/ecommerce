# Generated by Django 4.0.10 on 2024-02-20 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product3dblendermodel_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product3dblendermodel',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='model_3d', to='product.product'),
        ),
    ]
