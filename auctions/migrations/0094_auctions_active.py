# Generated by Django 4.0.5 on 2022-08-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0093_price_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]