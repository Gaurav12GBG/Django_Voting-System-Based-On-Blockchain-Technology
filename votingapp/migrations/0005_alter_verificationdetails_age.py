# Generated by Django 4.0 on 2022-05-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0004_verificationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationdetails',
            name='age',
            field=models.IntegerField(),
        ),
    ]