# Generated by Django 3.2.6 on 2021-08-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210824_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
