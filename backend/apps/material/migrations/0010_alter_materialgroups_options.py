# Generated by Django 4.0.10 on 2023-12-20 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0009_remove_material_color_materialgroups_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialgroups',
            options={'ordering': ('name',)},
        ),
    ]