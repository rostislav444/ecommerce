# Generated by Django 4.0.10 on 2023-12-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_alter_material_col_alter_material_nrm'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='refl',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
