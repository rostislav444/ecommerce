# Generated by Django 4.0.7 on 2022-11-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0004_alter_attributegroup_price_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributegroup',
            name='price_required',
            field=models.CharField(blank=True, choices=[('sub_group', 'sub_group'), ('attribute', 'attribute'), ('multiplier', 'multiplier'), ('sub_group_multiplier', 'sub_group_multiplier')], default=None, max_length=20, null=True),
        ),
    ]
