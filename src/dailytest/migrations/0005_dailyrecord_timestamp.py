# Generated by Django 2.1.1 on 2018-10-10 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dailytest', '0004_auto_20181008_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyrecord',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
