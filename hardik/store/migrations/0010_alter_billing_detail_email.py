# Generated by Django 4.2.3 on 2023-09-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_orders_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_detail',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
