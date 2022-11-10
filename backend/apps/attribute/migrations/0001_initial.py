# Generated by Django 4.0.7 on 2022-11-10 13:18

import apps.attribute.abstract.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('type', apps.attribute.abstract.fields.AttributeGroupTypeField(choices=[('text', 'Text'), ('integer', 'Integer'), ('boolean', 'Boolean'), ('float', 'Float'), ('color', 'Color'), ('range', 'Range'), ('image', 'Image')], default='text', max_length=24, verbose_name='Type')),
                ('custom', models.BooleanField(default=False)),
                ('price_required', models.CharField(blank=True, choices=[('sub_group', 'sub_group'), ('attribute', 'attribute')], default=None, max_length=9, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_groups', to='category.category')),
            ],
            options={
                'ordering': ['type', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeGroupUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeUnitGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('type', models.CharField(choices=[('string', 'String'), ('integer', 'Integer'), ('float', 'Float')], default='string', max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_group', to='attribute.attributegroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeSubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attributegroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attributegroup',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='attribute.attributegroupunit'),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Text')),
                ('value_integer', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Integer')),
                ('value_boolean', models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Boolean')),
                ('value_float', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Float')),
                ('value_color_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Color')),
                ('value_color_hex', colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=7, null=True, samples=None, verbose_name='Color HEX')),
                ('value_color_image', apps.attribute.abstract.fields.AttributeImageField(blank=True, null=True, storage=apps.attribute.abstract.fields.OverwriteStorage, upload_to='', verbose_name='Color IMAGE')),
                ('value_image_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Name')),
                ('value_image_image', apps.attribute.abstract.fields.AttributeImageField(blank=True, max_length=500, null=True, storage=apps.attribute.abstract.fields.OverwriteStorage, upload_to='', verbose_name='Image')),
                ('value_min', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Min')),
                ('value_max', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Max')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('manual', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('attribute_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='attribute.attributegroup')),
                ('sub_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='attribute.attributesubgroup')),
            ],
            options={
                'ordering': ('value_text', 'value_integer', 'value_boolean', 'value_float', 'value_color_name', 'value_min', 'value_max', 'value_image_name'),
                'abstract': False,
                'unique_together': {('attribute_group', 'value_min', 'value_max'), ('attribute_group', 'value_color_name', 'value_color_hex', 'value_color_image'), ('attribute_group', 'value_float'), ('attribute_group', 'value_integer'), ('attribute_group', 'value_text'), ('attribute_group', 'value_boolean')},
            },
        ),
        migrations.CreateModel(
            name='AttributeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_str', models.SlugField(blank=True, null=True)),
                ('value_int', models.PositiveIntegerField(blank=True, null=True)),
                ('value_float', models.FloatField(blank=True, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attribute.attribute')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attribute.attributeunitgroup')),
            ],
            options={
                'ordering': ('attribute', 'value_str', 'value_int', 'value_float'),
                'unique_together': {('unit', 'attribute', 'value_int'), ('unit', 'attribute'), ('unit', 'attribute', 'value_float')},
            },
        ),
    ]
