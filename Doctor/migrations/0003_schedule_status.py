# Generated by Django 2.2.1 on 2019-06-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_auto_20190605_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
