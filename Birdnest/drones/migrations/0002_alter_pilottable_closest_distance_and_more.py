# Generated by Django 4.0.6 on 2023-01-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilottable',
            name='closest_distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pilottable',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pilottable',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
