# Generated by Django 3.1.12 on 2025-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_auto_20250131_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
