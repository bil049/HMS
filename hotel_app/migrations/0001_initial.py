# Generated by Django 4.2 on 2023-05-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('confirm_password', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
