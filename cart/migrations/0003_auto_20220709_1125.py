# Generated by Django 3.2 on 2022-07-09 08:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_options',
            field=models.BooleanField(default=False),
        ),
    ]
