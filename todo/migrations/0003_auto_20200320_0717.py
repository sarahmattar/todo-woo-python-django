# Generated by Django 3.0.3 on 2020-03-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200320_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
