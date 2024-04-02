# Generated by Django 5.0.3 on 2024-04-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_guests',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], verbose_name='Guests numbers'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=10, unique=True, verbose_name='Room number'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(choices=[('single', 'Double'), ('double', 'Twin'), ('suite', 'Trio'), ('family', 'Family')], max_length=10, verbose_name='Room type'),
        ),
    ]