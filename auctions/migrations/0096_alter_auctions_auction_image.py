# Generated by Django 4.0.5 on 2022-08-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0095_auctions_buyer_alter_auctions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='Auction_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]