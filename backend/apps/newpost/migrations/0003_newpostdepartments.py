# Generated by Django 4.0.8 on 2022-11-25 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newpost', '0002_rename_newpoststates_newpostareas_newpostregion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPostDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_key', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('description_ru', models.CharField(max_length=255)),
                ('short_address', models.CharField(max_length=255)),
                ('short_address_ru', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=18)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=18)),
                ('schedule', models.JSONField(default={})),
                ('receiving_limitations_on_dimensions', models.JSONField(default={})),
                ('place_max_weight_allowed', models.PositiveIntegerField(default=0)),
                ('warehouse_status', models.CharField(max_length=255)),
                ('warehouse_index', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newpost.newpostcities')),
            ],
        ),
    ]