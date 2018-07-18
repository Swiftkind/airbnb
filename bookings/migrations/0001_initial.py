# Generated by Django 2.0.7 on 2018-07-12 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField(auto_now=True)),
                ('check_out_date', models.DateTimeField(auto_now=True)),
                ('number_of_guests', models.IntegerField(default=0)),
                ('number_of_nights', models.FloatField(default=0)),
                ('price_upon_booking', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('service_fee', models.FloatField(default=0)),
                ('total_amount_paid', models.FloatField(default=0)),
                ('is_canceled', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('property_rented', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Property')),
            ],
        ),
    ]
