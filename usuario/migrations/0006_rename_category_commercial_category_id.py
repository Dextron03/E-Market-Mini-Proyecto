# Generated by Django 5.0.1 on 2024-02-11 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_rename_id_category_commercial_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commercial',
            old_name='category',
            new_name='category_id',
        ),
    ]
