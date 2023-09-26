# Generated by Django 4.2.3 on 2023-09-18 11:59

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_user_image_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.AddField(
            model_name='orders',
            name='billing_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=store.models.billing_detail),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
