# Generated by Django 3.2.8 on 2021-10-22 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=515)),
                ('phone', models.CharField(max_length=515)),
                ('adharno', models.CharField(max_length=515)),
                ('voterid', models.CharField(max_length=515)),
                ('gender', models.CharField(max_length=515)),
                ('address', models.CharField(max_length=515)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
