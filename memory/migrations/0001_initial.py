# Generated by Django 4.2.4 on 2023-08-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelo_memory_goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.CharField(max_length=100)),
                ('_x', models.FloatField()),
                ('_y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='modelo_memory_obstacle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.CharField(max_length=100)),
                ('_x', models.FloatField()),
                ('_y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='modelo_memory_robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.CharField(max_length=100)),
                ('_x', models.FloatField()),
                ('_y', models.FloatField()),
            ],
        ),
    ]