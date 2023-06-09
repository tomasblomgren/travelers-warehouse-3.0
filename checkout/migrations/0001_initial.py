# Generated by Django 3.2 on 2023-03-23 14:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20230317_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()])),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{5}(?:-[0-9]{4})?$')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postcode', models.CharField(blank=True, max_length=50, null=True)),
                ('town_or_city', models.CharField(max_length=50)),
                ('street_adress1', models.CharField(max_length=50)),
                ('street_adress2', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]{13,19}$')])),
                ('expiry', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^(0[1-9]|1[0-2])\\/([0-9]{2})$')])),
                ('cvv', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^[0-9]{3,4}$')])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.payment'),
        ),
    ]
