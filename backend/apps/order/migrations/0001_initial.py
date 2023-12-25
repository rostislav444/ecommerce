# Generated by Django 4.0.8 on 2022-12-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0008_alter_productclassoption_value_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='product.product')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product_sku', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_value', models.JSONField(default=dict)),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productclassoption')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='order.orderproduct')),
            ],
        ),
    ]
