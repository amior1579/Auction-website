# Generated by Django 4.0.5 on 2022-08-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0086_alter_auctions_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='auctions',
        ),
        migrations.AddField(
            model_name='auctions',
            name='price',
            field=models.ManyToManyField(blank=True, default=None, related_name='auction_price', to='auctions.price'),
        ),
    ]