# Generated by Django 2.1.3 on 2018-12-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env_setting', '0002_auto_20181220_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfrecord',
            name='id',
        ),
        migrations.AddField(
            model_name='rfrecord',
            name='ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]