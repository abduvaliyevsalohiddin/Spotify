# Generated by Django 5.0 on 2023-12-11 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('sana', models.DateField(blank=True, null=True)),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tugulgan_yil', models.DateField()),
                ('davlat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('janr', models.CharField(max_length=30)),
                ('davomiylik', models.DurationField(blank=True, null=True)),
                ('fayl', models.FileField(null=True, upload_to='')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.qoshiqchi'),
        ),
    ]