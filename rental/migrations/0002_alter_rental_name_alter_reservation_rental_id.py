# Generated by Django 4.0.4 on 2022-05-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='name',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rental'),
        ),
    ]
