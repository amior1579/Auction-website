# Generated by Django 4.0.5 on 2022-07-29 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
