# Generated by Django 4.1.7 on 2023-03-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
