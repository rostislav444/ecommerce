# Generated by Django 4.0.10 on 2023-12-20 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_midcolor_color_ral_color_mid_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.color'),
        ),
    ]
