# Generated by Django 3.2.4 on 2021-06-27 00:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0007_alter_pet_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
