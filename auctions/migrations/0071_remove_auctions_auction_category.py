# Generated by Django 4.0.5 on 2022-08-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0070_remove_auctions_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='Auction_category',
        ),
    ]
