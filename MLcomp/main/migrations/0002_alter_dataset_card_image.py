# Generated by Django 3.2.6 on 2021-08-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='card_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
