# Generated by Django 4.2.8 on 2024-02-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordApp', '0008_alter_passwordmanagerdatamodel_safebox'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordmanagerdatamodel',
            name='userName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
