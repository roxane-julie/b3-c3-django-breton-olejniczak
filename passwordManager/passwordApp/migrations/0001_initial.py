# Generated by Django 4.2.8 on 2024-02-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassWordManagerDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('websiteName', models.CharField(max_length=100)),
                ('websiteUrl', models.URLField(blank=True, default='')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
