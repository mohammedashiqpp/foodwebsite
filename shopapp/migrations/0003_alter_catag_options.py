# Generated by Django 3.2.6 on 2021-08-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catag',
            options={'ordering': ('name',), 'verbose_name': 'cata', 'verbose_name_plural': 'catagory'},
        ),
    ]
