# Generated by Django 4.0.5 on 2022-08-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0077_auctions_user_alter_auctions_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]