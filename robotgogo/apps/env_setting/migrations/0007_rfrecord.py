# Generated by Django 2.1.3 on 2018-12-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env_setting', '0006_delete_rfrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='rfrecord',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('envName', models.CharField(max_length=20)),
                ('TestModel', models.CharField(max_length=20)),
                ('email1', models.CharField(max_length=100)),
                ('email2', models.CharField(max_length=100)),
                ('email3', models.CharField(max_length=100)),
                ('TestTime', models.CharField(max_length=20)),
                ('autopush', models.BooleanField(default=False)),
            ],
        ),
    ]
