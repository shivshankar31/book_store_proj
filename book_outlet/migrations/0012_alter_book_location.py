# Generated by Django 3.2.9 on 2021-12-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0011_auto_20211201_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.ManyToManyField(to='book_outlet.Location'),
        ),
    ]
