# Generated by Django 5.1.1 on 2024-09-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('farm', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('profile', models.CharField(blank=True, max_length=200, null=True)),
                ('roast', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
