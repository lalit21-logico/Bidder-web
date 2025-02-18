# Generated by Django 3.1.1 on 2020-09-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BidderWeb', '0002_auto_20200929_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('base_price', models.IntegerField(max_length=20)),
                ('high_price', models.IntegerField(max_length=20)),
                ('buyer_id', models.IntegerField(max_length=20)),
                ('information', models.CharField(max_length=500)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('user_id', models.IntegerField(max_length=20)),
            ],
        ),
    ]
