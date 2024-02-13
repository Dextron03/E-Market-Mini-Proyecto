# Generated by Django 5.0.2 on 2024-02-12 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_commercial_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='commercial_images/')),
                ('commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='usuario.commercial')),
            ],
        ),
    ]