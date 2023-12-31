# Generated by Django 4.1.3 on 2023-09-12 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contactpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('msg', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('discount_amount', models.IntegerField()),
                ('min_order_amount', models.IntegerField()),
                ('max_order_amount', models.IntegerField()),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='filter_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_range', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='main_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='man-3.jpg', upload_to='photo')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=123)),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.main_category')),
            ],
        ),
        migrations.CreateModel(
            name='product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qtn', models.IntegerField()),
                ('brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('color', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.color')),
                ('filter_price', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.filter_price')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.main_category')),
                ('size', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.size')),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('qtn', models.IntegerField()),
                ('product_total', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='billing_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contry', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('uid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='add_to_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo')),
                ('pro_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('qtn', models.IntegerField()),
                ('total', models.IntegerField()),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product1')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
    ]
