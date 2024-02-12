# Generated by Django 5.0.1 on 2024-02-07 05:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_myuser_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('img', models.ImageField(blank=True, default='media/profile.jpg', null=True, upload_to='media/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.category')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]