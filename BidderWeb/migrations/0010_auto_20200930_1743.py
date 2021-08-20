# Generated by Django 3.1.1 on 2020-09-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BidderWeb', '0009_watchist_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchist_data',
            name='user_id',
        ),
        migrations.AddField(
            model_name='watchist_data',
            name='watch_user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
