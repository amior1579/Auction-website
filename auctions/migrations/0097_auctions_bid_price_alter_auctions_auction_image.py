# Generated by Django 4.0.5 on 2022-08-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0096_alter_auctions_auction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='bid_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctions',
            name='Auction_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
