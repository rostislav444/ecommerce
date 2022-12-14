# Generated by Django 4.0.7 on 2022-11-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewPostApiKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NewPostStates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=255)),
                ('areas_center', models.CharField(max_length=255)),
                ('description_ru', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('description', 'description_ru'),
            },
        ),
    ]
