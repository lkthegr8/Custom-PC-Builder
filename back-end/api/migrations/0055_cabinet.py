# Generated by Django 3.1.7 on 2021-05-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_auto_20210428_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='CABINET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('imageurl', models.CharField(max_length=100)),
            ],
        ),
    ]
