# Generated by Django 4.0.5 on 2022-07-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_auctions_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='Auction_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
