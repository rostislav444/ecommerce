# Generated by Django 4.0.10 on 2024-02-23 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_productpartscenematerial_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpartscenematerial',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='product.productpartscene'),
        ),
    ]
