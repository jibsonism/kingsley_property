# Generated by Django 4.2 on 2023-04-17 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
    ]