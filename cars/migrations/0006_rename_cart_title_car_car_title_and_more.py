# Generated by Django 5.0.3 on 2024-03-06 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='cart_title',
            new_name='car_title',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='mils',
            new_name='miles',
        ),
    ]
