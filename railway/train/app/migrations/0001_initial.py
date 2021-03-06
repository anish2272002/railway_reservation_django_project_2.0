# Generated by Django 3.2 on 2021-05-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
