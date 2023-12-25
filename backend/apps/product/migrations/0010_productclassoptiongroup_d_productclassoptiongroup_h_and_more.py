# Generated by Django 4.0.10 on 2023-10-21 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productclass_depth_step_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclassoptiongroup',
            name='d',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productclassoptiongroup',
            name='h',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productclassoptiongroup',
            name='w',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productclass',
            name='max_depth',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Max depth'),
        ),
        migrations.AlterField(
            model_name='productclass',
            name='min_height',
            field=models.PositiveIntegerField(default=0, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='productclass',
            name='min_width',
            field=models.PositiveIntegerField(default=0, verbose_name='Width'),
        ),
    ]
