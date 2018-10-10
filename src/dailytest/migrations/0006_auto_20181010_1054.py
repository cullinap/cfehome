# Generated by Django 2.1.1 on 2018-10-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytest', '0005_dailyrecord_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyrecord',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
