# Generated by Django 4.0.7 on 2022-11-17 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productoptionpricemultiplier_option_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productclassoptiongroup',
            name='quantity',
        ),
    ]