# Generated by Django 4.0.5 on 2022-07-31 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0051_remove_comments_comment_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions'),
        ),
    ]
