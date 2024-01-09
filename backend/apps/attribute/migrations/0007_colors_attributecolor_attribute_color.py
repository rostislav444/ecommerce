# Generated by Django 4.0.8 on 2022-12-05 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0006_alter_attributesubgroup_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=1024, null=True)),
                ('hex', models.CharField(max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='attribute.attributegroup')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.colors')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='attribute.attributecolor'),
        ),
    ]