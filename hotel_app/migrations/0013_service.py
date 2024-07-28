# Generated by Django 4.2 on 2023-05-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0012_message_delete_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Pick-Up', 'Pick-Up'), ('Drop-Off', 'Drop-Off')], max_length=120, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
    ]
