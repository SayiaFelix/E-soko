# Generated by Django 3.2 on 2022-07-09 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0008_auto_20220709_1232'),
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
            field=models.BooleanField(choices=[('M-Pesa', 'M-Pesa'), ('PayPal', 'PayPal'), ('Stripe', 'Stripe')], default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
