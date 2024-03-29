# Generated by Django 4.0.10 on 2024-02-23 21:21

import apps.abstract.fields.fields_image
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productpartscene_productpartscenematerial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpartscenematerial',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductPartSceneMaterialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', apps.abstract.fields.fields_image.DeletableImageField(upload_to='')),
                ('scene_material', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.productpartscenematerial')),
            ],
        ),
    ]
