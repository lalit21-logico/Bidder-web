# Generated by Django 3.1.1 on 2020-09-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BidderWeb', '0011_auto_20200930_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist_data',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BidderWeb.product_data'),
        ),
    ]