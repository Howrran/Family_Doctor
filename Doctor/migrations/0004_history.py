# Generated by Django 2.2.1 on 2019-06-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_schedule_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('desease', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]