# Generated by Django 4.2.3 on 2023-09-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
