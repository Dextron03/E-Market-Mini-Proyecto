# Generated by Django 5.0.1 on 2024-02-11 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commercial',
            old_name='id_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='commercial',
            old_name='id_user',
            new_name='user',
        ),
    ]