# Generated by Django 4.0.5 on 2022-08-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0081_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='Auction_description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
