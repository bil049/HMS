# Generated by Django 4.2 on 2023-05-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_reservation_delete_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Executive', 'Executive'), ('Adjoining', 'Adjoining'), ('Presidential Suite', 'Presidential Suite')], max_length=120, null=True),
        ),
    ]
