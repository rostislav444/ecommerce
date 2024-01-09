# Generated by Django 4.0.10 on 2023-11-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0015_remove_attributegroup_category'),
        ('product', '0013_alter_productclassproductattributegroups_use_all_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclassoption',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productclassoptiongroup',
            name='price_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='productclassproductattributes',
            unique_together={('attribute_group', 'attribute')},
        ),
    ]