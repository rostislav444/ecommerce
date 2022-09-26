# Generated by Django 4.0.7 on 2022-09-26 13:49

import apps.attribute.abstract.fields
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0004_rename_group_attribute_attribute_group_and_more'),
        ('product', '0008_alter_productclassoptiongroup_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productclassattributes',
            options={'ordering': ('value_text', 'value_integer', 'value_boolean', 'value_float', 'value_color_name', 'value_min', 'value_max', 'value_image_name')},
        ),
        migrations.AlterModelOptions(
            name='skuoptions',
            options={'ordering': ('sku', 'option')},
        ),
        migrations.RenameField(
            model_name='productattribute',
            old_name='group',
            new_name='attribute_group',
        ),
        migrations.RenameField(
            model_name='productclassoption',
            old_name='group',
            new_name='attribute_group',
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_boolean',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Boolean'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_color_hex',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=7, null=True, samples=None, verbose_name='Color HEX'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_color_image',
            field=apps.attribute.abstract.fields.AttributeImageField(blank=True, null=True, storage=apps.attribute.abstract.fields.OverwriteStorage, upload_to='', verbose_name='Color IMAGE'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_color_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_float',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Float'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_image_image',
            field=apps.attribute.abstract.fields.AttributeImageField(blank=True, max_length=500, null=True, storage=apps.attribute.abstract.fields.OverwriteStorage, upload_to='', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_image_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_integer',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Integer'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_max',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Max'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_min',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Min'),
        ),
        migrations.AddField(
            model_name='productclassattributes',
            name='value_text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Text'),
        ),
        migrations.AlterUniqueTogether(
            name='productattribute',
            unique_together={('attribute_group', 'value_min', 'value_max'), ('attribute_group', 'value_text'), ('attribute_group', 'value_attribute'), ('attribute_group', 'value_boolean'), ('attribute_group', 'value_integer'), ('attribute_group', 'value_color_name', 'value_color_hex', 'value_color_image'), ('attribute_group', 'value_float')},
        ),
        migrations.AlterUniqueTogether(
            name='productclassattributes',
            unique_together={('attribute_group', 'value_min', 'value_max'), ('attribute_group', 'value_text'), ('attribute_group', 'value_boolean'), ('attribute_group', 'value_integer'), ('attribute_group', 'value_color_name', 'value_color_hex', 'value_color_image'), ('attribute_group', 'value_float')},
        ),
        migrations.AlterUniqueTogether(
            name='productclassoption',
            unique_together={('attribute_group', 'value_min', 'value_max'), ('attribute_group', 'value_text'), ('attribute_group', 'value_attribute'), ('attribute_group', 'value_boolean'), ('attribute_group', 'value_integer'), ('attribute_group', 'value_color_name', 'value_color_hex', 'value_color_image'), ('attribute_group', 'value_float')},
        ),
    ]
