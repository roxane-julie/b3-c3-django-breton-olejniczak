# Generated by Django 4.2.8 on 2024-02-18 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passwordApp', '0009_passwordmanagerdatamodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordmanagerdatamodel',
            name='safebox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='password_data', to='passwordApp.safebox'),
        ),
    ]