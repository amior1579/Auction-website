# Generated by Django 4.0.5 on 2022-08-02 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0057_remove_comments_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.auctions'),
        ),
    ]
