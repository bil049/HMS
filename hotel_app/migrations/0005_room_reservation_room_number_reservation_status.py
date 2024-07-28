# Generated by Django 4.2 on 2023-05-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_reservation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(null=True)),
                ('room_type', models.CharField(choices=[('Standard', 'Standard'), ('Executive', 'Executive'), ('Adjoining', 'Adjoining'), ('Presidential Suite', 'Presidential Suite')], max_length=120, null=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')], max_length=120, null=True),
        ),
    ]
