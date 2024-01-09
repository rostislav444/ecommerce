# Generated by Django 4.0.10 on 2023-12-30 13:27

import apps.abstract.fields.fields_image
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_alter_productpartmaterials_options_alter_sku_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skuimages',
            name='image_thumb',
        ),
        migrations.AlterField(
            model_name='skuimages',
            name='image',
            field=apps.abstract.fields.fields_image.DeletableImageField(upload_to=''),
        ),
    ]