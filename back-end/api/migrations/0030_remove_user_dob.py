# Generated by Django 3.1.7 on 2021-04-26 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
