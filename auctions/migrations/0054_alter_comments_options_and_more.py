# Generated by Django 4.0.5 on 2022-08-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0053_alter_comments_options_comments_auction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['date_added']},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Auction',
            new_name='auction',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='created_on',
            new_name='date_added',
        ),
    ]
