# Generated by Django 4.2.5 on 2023-10-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='status',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
