# Generated by Django 2.2.4 on 2019-09-03 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190903_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_client_id', to='news.Client'),
        ),
    ]
