# Generated by Django 3.0.5 on 2020-04-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productelektronik',
            name='merk',
        ),
        migrations.RemoveField(
            model_name='productelektronik',
            name='warna',
        ),
        migrations.RemoveField(
            model_name='productotomotif',
            name='merk',
        ),
        migrations.RemoveField(
            model_name='productotomotif',
            name='warna',
        ),
        migrations.AlterField(
            model_name='productotomotif',
            name='spek',
            field=models.TextField(),
        ),
    ]