# Generated by Django 4.0.5 on 2022-08-01 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0052_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comments',
            name='Auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.auctions'),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
        ),
    ]
