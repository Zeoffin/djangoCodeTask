# Generated by Django 4.0.4 on 2022-05-15 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_rental_name_alter_reservation_rental_id'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='reservation',
            order_with_respect_to='checkout',
        ),
    ]