# Generated by Django 2.1.1 on 2018-10-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyrecord',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]