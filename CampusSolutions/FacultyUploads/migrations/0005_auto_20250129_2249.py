# Generated by Django 3.1.12 on 2025-01-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyUploads', '0004_auto_20250129_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='Type',
            new_name='type',
        ),
    ]
