# Generated by Django 3.2.6 on 2021-08-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_item_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='qlt',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
